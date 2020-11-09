#  Copyright (c) 2020 JD Williams
#
#  This file is part of Firefly, a Python SOA framework built by JD Williams. Firefly is free software; you can
#  redistribute it and/or modify it under the terms of the GNU General Public License as published by the
#  Free Software Foundation; either version 3 of the License, or (at your option) any later version.
#
#  Firefly is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
#  implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
#  Public License for more details. You should have received a copy of the GNU Lesser General Public
#  License along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#  You should have received a copy of the GNU General Public License along with Firefly. If not, see
#  <http://www.gnu.org/licenses/>.

from __future__ import annotations

import inspect
import json
import re
from pprint import pprint
from typing import Union

import firefly as ff
import firefly_aws.domain as domain


STATUS_CODES = {
    'BadRequest': 400,
    'Unauthorized': 401,
    'Forbidden': 403,
    'NotFound': 404,
    'ApiError': 500,
}

ACCESS_CONTROL_HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
    'Access-Control-Allow-Headers': 'Authorization, Accept, Accept-Language, Content-Language, Content-Type',
}

COGNITO_TRIGGERS = (
    'PreSignUp_SignUp', 'PreSignUp_AdminCreateUser', 'PostConfirmation_ConfirmSignUp',
    'PostConfirmation_ConfirmForgotPassword', 'PreAuthentication_Authentication', 'PostAuthentication_Authentication',
    'DefineAuthChallenge_Authentication', 'CreateAuthChallenge_Authentication',
    'VerifyAuthChallengeResponse_Authentication', 'TokenGeneration_HostedAuth', 'TokenGeneration_Authentication',
    'TokenGeneration_NewPasswordChallenge', 'TokenGeneration_AuthenticateDevice', 'TokenGeneration_RefreshTokens',
    'UserMigration_Authentication', 'UserMigration_ForgotPassword', 'CustomMessage_SignUp',
    'CustomMessage_AdminCreateUser', 'CustomMessage_ResendCode', 'CustomMessage_ForgotPassword',
    'CustomMessage_UpdateUserAttribute', 'CustomMessage_VerifyUserAttribute', 'CustomMessage_Authentication'
)


class LambdaExecutor(ff.DomainService):
    _serializer: ff.Serializer = None
    _message_factory: ff.MessageFactory = None
    _rest_router: ff.RestRouter = None
    _s3_client = None
    _s3_service: domain.S3Service = None
    _bucket: str = None

    def __init__(self):
        self._version_matcher = re.compile(r'^/v\d')

    def run(self, event: dict, context: dict):
        self.debug('Event: %s', event)
        self.debug('Context: %s', context)

        if 'requestContext' in event and 'http' in event['requestContext']:
            self.info('HTTP request')
            return self._handle_http_event(event)

        if 'Records' in event and 'aws:sqs' == event['Records'][0].get('eventSource'):
            self.info('SQS message')
            return self._handle_sqs_event(event)

        try:
            message = False
            aws_message = False
            if self._is_cognito_trigger_event(event):
                aws_message = True
                message = self._generate_cognito_trigger_messages(event)
                if message is False:
                    self.debug('Passing through cognito trigger event')
                    return event

            if message is False:
                message = self._serializer.deserialize(json.dumps(event))
            if isinstance(message, ff.Command):
                try:
                    return self.invoke(message)
                except ff.ConfigurationError:
                    if aws_message is True:
                        return event
                    raise
            elif isinstance(message, ff.Query):
                return self.request(message)
        except:
            pass

        return {
            'statusCode': 200,
            'headers': ACCESS_CONTROL_HEADERS,
            'body': '',
            'isBase64Encoded': False,
        }

    def _handle_http_event(self, event: dict):
        route = self._version_matcher.sub('', event['rawPath'])
        method = event['requestContext']['http']['method']

        if method.lower() == 'options':
            return {
                'statusCode': 200,
                'headers': ACCESS_CONTROL_HEADERS,
            }

        body = None
        if 'body' in event:
            for k, v in event['headers'].items():
                if k.lower() == 'content-type':
                    if 'application/json' in v.lower():
                        body = self._serializer.deserialize(event['body'])
                    else:
                        body = event['body']
            if body is None:
                body = self._serializer.deserialize(event['body'])

        try:
            self.info(f'Trying to match route: "{method} {route}"')
            endpoint, params = self._rest_router.match(route, method)
            if not endpoint:
                return {'statusCode': 404}

            if endpoint.message is not None:
                message_name = endpoint.message if isinstance(endpoint.message, str) else endpoint.message.get_fqn()
            else:
                message_name = endpoint.service
                if inspect.isclass(message_name):
                    message_name = message_name.get_fqn()
            self.info(f'Matched route')

            if 'queryStringParameters' in event:
                params.update(event['queryStringParameters'])

            params['headers'] = {
                'http_request': {
                    'headers': event['headers'],
                },
                'secured': endpoint.secured,
                'scopes': endpoint.scopes,
            }

            try:
                if method.lower() == 'get':
                    return self._handle_http_response(self.request(message_name, data=params))
                else:
                    if body is not None:
                        if isinstance(body, dict):
                            params.update(body)
                        else:
                            params['body'] = body
                    return self._handle_http_response(self.invoke(message_name, params))
            except ff.UnauthenticatedError:
                self.info('Unauthenticated')
                return {'statusCode': 403}
            except ff.UnauthorizedError:
                self.info('Unauthorized')
                return {'statusCode': 401}
            except ff.ApiError as e:
                return self._handle_http_response(str(e), status_code=STATUS_CODES[e.__class__.__name__])

        except TypeError:
            pass

    def _handle_http_response(self, response: any, status_code: int = 200, headers: dict = None):
        headers = headers or {}
        headers.update(ACCESS_CONTROL_HEADERS)
        body = self._serializer.serialize(response)
        ret = {
            'statusCode': status_code,
            'headers': headers,
            'body': body,
            'isBase64Encoded': False,
        }

        if len(body) > 10000000:
            download_url = self._s3_service.store_download(body, apply_compression=False)
            ret['body'] = json.dumps({
                'location': download_url
            })
            ret['statusCode'] = 303
            ret['headers']['Location'] = download_url

        self.info(f'Proxy Response: %s', ret)
        return ret

    def _handle_sqs_event(self, event: dict):
        for record in event['Records']:
            body = self._serializer.deserialize(record['body'])
            message: Union[ff.Event, dict] = self._serializer.deserialize(body['Message'])

            if isinstance(message, dict) and 'PAYLOAD_KEY' in message:
                try:
                    message = self.load_payload(message['PAYLOAD_KEY'])
                except Exception as e:
                    self.nack_message(record)
                    self.error(e)
                    continue
            if message is None:
                self.info('Got a null message')
                return

            message.headers['external'] = True
            self.dispatch(message)
        if len(event['Records']) == 1:
            self.complete_handshake(event['Records'][0])
        else:
            self.complete_batch_handshake(event['Records'])

    @staticmethod
    def _is_cognito_trigger_event(event: dict):
        return 'triggerSource' in event

    def _generate_cognito_trigger_messages(self, event: dict):
        if event['triggerSource'] in COGNITO_TRIGGERS:
            return self._message_factory.command(f'firefly_aws.{event["triggerSource"]}', data={
                'event': event
            })

        return False

    def load_payload(self, key: str):
        response = self._s3_client.get_object(
            Bucket=self._bucket,
            Key=key
        )
        return self._serializer.deserialize(response['Body'].read())

    def nack_message(self, record: dict):
        pass

    def complete_handshake(self, record: dict):
        pass

    def complete_batch_handshake(self, records: list):
        pass
