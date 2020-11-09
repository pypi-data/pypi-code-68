import pytest
from flask import Flask, jsonify

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, set_access_cookies
)


@pytest.fixture(scope='function')
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'foobarbaz'
    app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies', 'query_string', 'json']
    JWTManager(app)

    @app.route('/cookie_login', methods=['GET'])
    def cookie_login():
        resp = jsonify(login=True)
        access_token = create_access_token('username')
        set_access_cookies(resp, access_token)
        return resp

    @app.route('/protected', methods=['GET', 'POST'])
    @jwt_required
    def access_protected():
        return jsonify(foo='bar')

    return app


def test_header_access(app):
    test_client = app.test_client()
    with app.test_request_context():
        access_token = create_access_token('username')

    access_headers = {'Authorization': 'Bearer {}'.format(access_token)}
    response = test_client.get('/protected', headers=access_headers)
    assert response.status_code == 200
    assert response.get_json() == {'foo': 'bar'}


def test_cookie_access(app):
    test_client = app.test_client()
    test_client.get('/cookie_login')
    response = test_client.get('/protected')
    assert response.status_code == 200
    assert response.get_json() == {'foo': 'bar'}


def test_query_string_access(app):
    test_client = app.test_client()
    with app.test_request_context():
        access_token = create_access_token('username')

    url = '/protected?jwt={}'.format(access_token)
    response = test_client.get(url)
    assert response.status_code == 200
    assert response.get_json() == {'foo': 'bar'}


def test_json_access(app):
    test_client = app.test_client()

    with app.test_request_context():
        access_token = create_access_token('username')

    data = {'access_token': access_token}
    response = test_client.post('/protected', json=data)
    assert response.status_code == 200
    assert response.get_json() == {'foo': 'bar'}


@pytest.mark.parametrize("options", [
    (['cookies', 'headers'], ('Missing JWT in cookies or headers (Missing cookie '
                              '"access_token_cookie"; Missing Authorization Header)')),
    (['json', 'query_string'], ('Missing JWT in json or query_string (Invalid '
                                'content-type. Must be application/json.; '
                                'Missing "jwt" query paramater)')),
])
def test_no_jwt_in_request(app, options):
    token_locations, expected_err = options
    app.config['JWT_TOKEN_LOCATION'] = token_locations
    test_client = app.test_client()
    response = test_client.get('/protected')
    assert response.status_code == 401
    assert response.get_json() == {'msg': expected_err}


@pytest.mark.parametrize("options", [
    (['cookies', 'headers'], 200, None, {'foo': 'bar'}),
    (['headers', 'cookies'], 200, None, {'foo': 'bar'}),
])
def test_order_of_jwt_locations_in_request(app, options):
    """ test order doesn't matter if at least one valid token is set"""
    token_locations, status_code, expected_err, expected_dict = options
    app.config['JWT_TOKEN_LOCATION'] = token_locations
    test_client = app.test_client()
    test_client.get('/cookie_login')
    response = test_client.get('/protected')

    assert response.status_code == status_code
    if expected_dict:
        assert response.get_json() == expected_dict
    else:
        assert response.get_json() == {'msg': expected_err}


@pytest.mark.parametrize("options", [
    (['cookies', 'headers'], 200, None, {'foo': 'bar'}),
    (['headers', 'cookies'], 422, ('Invalid header padding'), None),
])
def test_order_of_jwt_locations_with_one_invalid_token_in_request(app, options):
    """ test order doesn't matter if at least one valid token is set"""
    token_locations, status_code, expected_err, expected_dict = options
    app.config['JWT_TOKEN_LOCATION'] = token_locations
    test_client = app.test_client()

    with app.test_request_context():
        access_token = create_access_token('username')
    # invalidate the token, to check token location precedence
    access_token = "000000{}".format(access_token[5:])
    access_headers = {'Authorization': 'Bearer {}'.format(access_token)}
    # set valid cookies
    test_client.get('/cookie_login')
    response = test_client.get('/protected', headers=access_headers)

    assert response.status_code == status_code
    if expected_dict:
        assert response.get_json() == expected_dict
    else:
        assert response.get_json() == {'msg': expected_err}
