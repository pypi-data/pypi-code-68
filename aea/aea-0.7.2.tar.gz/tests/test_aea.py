# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
"""This module contains the tests for aea/aea.py."""
import os
import tempfile
import time
import unittest
from pathlib import Path
from threading import Thread
from typing import Callable
from unittest.case import TestCase
from unittest.mock import patch

import pytest

from aea.aea import AEA
from aea.aea_builder import AEABuilder
from aea.configurations.base import SkillConfig
from aea.configurations.constants import DEFAULT_LEDGER, DEFAULT_PRIVATE_KEY_FILE
from aea.crypto.wallet import Wallet
from aea.exceptions import AEAException
from aea.helpers.exception_policy import ExceptionPolicyEnum
from aea.identity.base import Identity
from aea.mail.base import Envelope
from aea.protocols.base import Protocol
from aea.registries.resources import Resources
from aea.runtime import RuntimeStates, _StopRuntime
from aea.skills.base import Skill, SkillContext

from packages.fetchai.connections.local.connection import LocalNode, OEFLocalConnection
from packages.fetchai.protocols.default.message import DefaultMessage
from packages.fetchai.protocols.default.serialization import DefaultSerializer
from packages.fetchai.protocols.fipa.message import FipaMessage

from tests.common.utils import (
    AeaTool,
    make_behaviour_cls_from_funcion,
    make_handler_cls_from_funcion,
    run_in_thread,
    timeit_context,
    wait_for_condition,
)
from tests.conftest import (
    CUR_PATH,
    FETCHAI_PRIVATE_KEY_PATH,
    ROOT_DIR,
    UNKNOWN_PROTOCOL_PUBLIC_ID,
    _make_local_connection,
)
from tests.data.dummy_aea.skills.dummy.tasks import DummyTask  # type: ignore
from tests.data.dummy_skill import PUBLIC_ID as DUMMY_SKILL_PUBLIC_ID
from tests.data.dummy_skill.behaviours import DummyBehaviour  # type: ignore


def test_setup_aea():
    """Tests the initialisation of the AEA."""
    private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
    builder = AEABuilder()
    builder.set_name("my_name").add_private_key(DEFAULT_LEDGER, private_key_path)
    my_AEA = builder.build()
    assert my_AEA.context == my_AEA._context, "Cannot access the Agent's Context"
    assert (
        not my_AEA.context.connection_status.is_connected
    ), "AEA should not be connected."
    my_AEA.setup()
    assert my_AEA.resources is not None, "Resources must not be None after setup"
    my_AEA.resources = Resources()
    assert my_AEA.resources is not None, "Resources must not be None after set"
    assert (
        my_AEA.context.shared_state is not None
    ), "Shared state must not be None after set"
    assert my_AEA.context.task_manager is not None
    assert my_AEA.context.identity is not None, "Identity must not be None after set."
    my_AEA.teardown()


def test_act():
    """Tests the act function of the AEA."""
    agent_name = "MyAgent"
    private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
    builder = AEABuilder()
    builder.set_name(agent_name)
    builder.add_private_key(DEFAULT_LEDGER, private_key_path)
    builder.add_skill(Path(CUR_PATH, "data", "dummy_skill"))
    agent = builder.build()

    with run_in_thread(agent.start, timeout=20):
        wait_for_condition(lambda: agent.is_running, timeout=20)
        behaviour = agent.resources.get_behaviour(DUMMY_SKILL_PUBLIC_ID, "dummy")

        time.sleep(1)
        wait_for_condition(lambda: behaviour.nb_act_called > 0, timeout=20)
        agent.stop()


def test_start_stop():
    """Tests the act function of the AEA."""
    agent_name = "MyAgent"
    private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
    builder = AEABuilder()
    builder.set_name(agent_name)
    builder.add_private_key(DEFAULT_LEDGER, private_key_path)
    builder.add_skill(Path(CUR_PATH, "data", "dummy_skill"))
    agent = builder.build()

    with run_in_thread(agent.start, timeout=20):
        wait_for_condition(lambda: agent.is_running, timeout=20)
        agent.stop()


def test_double_start():
    """Tests the act function of the AEA."""
    agent_name = "MyAgent"
    private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
    builder = AEABuilder()
    builder.set_name(agent_name)
    builder.add_private_key(DEFAULT_LEDGER, private_key_path)
    builder.add_skill(Path(CUR_PATH, "data", "dummy_skill"))
    agent = builder.build()

    with run_in_thread(agent.start, timeout=20):
        try:
            wait_for_condition(lambda: agent.is_running, timeout=20)
            t = Thread(target=agent.start)
            t.start()
            time.sleep(1)
            assert not t.is_alive()
        finally:
            agent.stop()


def test_react():
    """Tests income messages."""
    with LocalNode() as node:
        agent_name = "MyAgent"
        private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
        builder = AEABuilder()
        builder.set_name(agent_name)
        builder.add_private_key(DEFAULT_LEDGER, private_key_path)
        builder.add_protocol(
            Path(ROOT_DIR, "packages", "fetchai", "protocols", "oef_search")
        )
        builder.add_connection(
            Path(ROOT_DIR, "packages", "fetchai", "connections", "local")
        )
        local_connection_id = OEFLocalConnection.connection_id
        builder.set_default_connection(local_connection_id)
        builder.add_skill(Path(CUR_PATH, "data", "dummy_skill"))
        agent = builder.build(connection_ids=[local_connection_id])
        # This is a temporary workaround to feed the local node to the OEF Local connection
        # TODO remove it.
        local_connection = agent.resources.get_connection(local_connection_id)
        local_connection._local_node = node

        msg = DefaultMessage(
            dialogue_reference=("", ""),
            message_id=1,
            target=0,
            performative=DefaultMessage.Performative.BYTES,
            content=b"hello",
        )
        msg.to = agent.identity.address
        msg.sender = agent.identity.address
        envelope = Envelope(
            to=msg.to, sender=msg.sender, protocol_id=msg.protocol_id, message=msg,
        )

        with run_in_thread(agent.start, timeout=20, on_exit=agent.stop):
            wait_for_condition(lambda: agent.is_running, timeout=20)
            agent.outbox.put(envelope)
            default_protocol_public_id = DefaultMessage.protocol_id
            dummy_skill_public_id = DUMMY_SKILL_PUBLIC_ID
            handler = agent.resources.get_handler(
                default_protocol_public_id, dummy_skill_public_id
            )

            assert handler is not None, "Handler is not set."

            wait_for_condition(
                lambda: len(handler.handled_messages) > 0,
                timeout=20,
                error_msg="The message is not inside the handled_messages.",
            )


def test_handle():
    """Tests handle method of an agent."""
    with LocalNode() as node:
        agent_name = "MyAgent"
        private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
        builder = AEABuilder()
        builder.set_name(agent_name)
        builder.add_private_key(DEFAULT_LEDGER, private_key_path)
        builder.add_protocol(
            Path(ROOT_DIR, "packages", "fetchai", "protocols", "oef_search")
        )
        builder.add_connection(
            Path(ROOT_DIR, "packages", "fetchai", "connections", "local")
        )
        local_connection_id = OEFLocalConnection.connection_id
        builder.set_default_connection(local_connection_id)
        builder.add_skill(Path(CUR_PATH, "data", "dummy_skill"))
        aea = builder.build(connection_ids=[local_connection_id])
        # This is a temporary workaround to feed the local node to the OEF Local connection
        # TODO remove it.
        local_connection = aea.resources.get_connection(local_connection_id)
        local_connection._local_node = node

        msg = DefaultMessage(
            dialogue_reference=("", ""),
            message_id=1,
            target=0,
            performative=DefaultMessage.Performative.BYTES,
            content=b"hello",
        )
        msg.to = aea.identity.address
        msg.sender = aea.identity.address

        encoded_msg = DefaultSerializer.encode(msg)
        envelope = Envelope(
            to=msg.to,
            sender=msg.sender,
            protocol_id=UNKNOWN_PROTOCOL_PUBLIC_ID,
            message=msg,
        )

        with run_in_thread(aea.start, timeout=5):
            wait_for_condition(lambda: aea.is_running, timeout=10)
            dummy_skill = aea.resources.get_skill(DUMMY_SKILL_PUBLIC_ID)
            dummy_handler = dummy_skill.handlers["dummy"]

            aea.outbox.put(envelope)

            wait_for_condition(
                lambda: len(dummy_handler.handled_messages) == 1, timeout=1,
            )

            #   DECODING ERROR
            envelope = Envelope(
                to=aea.identity.address,
                sender=aea.identity.address,
                protocol_id=DefaultMessage.protocol_id,
                message=b"",
            )
            # send envelope via localnode back to agent/bypass `outbox` put consistency checks
            aea.outbox._multiplexer.put(envelope)
            """ inbox twice cause first message is invalid. generates error message and it accepted """
            wait_for_condition(
                lambda: len(dummy_handler.handled_messages) == 2, timeout=1,
            )
            #   UNSUPPORTED SKILL
            msg = FipaMessage(
                performative=FipaMessage.Performative.ACCEPT,
                message_id=1,
                dialogue_reference=(str(0), ""),
                target=0,
            )
            msg.to = aea.identity.address
            msg.sender = aea.identity.address
            envelope = Envelope(
                to=msg.to, sender=msg.sender, protocol_id=msg.protocol_id, message=msg,
            )
            # send envelope via localnode back to agent
            aea.outbox.put(envelope)
            wait_for_condition(
                lambda: len(dummy_handler.handled_messages) == 3, timeout=2,
            )

            #   DECODING OK
            envelope = Envelope(
                to=msg.to,
                sender=msg.sender,
                protocol_id=DefaultMessage.protocol_id,
                message=encoded_msg,
            )
            # send envelope via localnode back to agent/bypass `outbox` put consistency checks
            aea.outbox._multiplexer.put(envelope)
            wait_for_condition(
                lambda: len(dummy_handler.handled_messages) == 4, timeout=1,
            )
            aea.stop()


def test_initialize_aea_programmatically():
    """Test that we can initialize an AEA programmatically."""
    with LocalNode() as node:
        agent_name = "MyAgent"
        private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
        builder = AEABuilder()
        builder.set_name(agent_name)
        builder.add_private_key(DEFAULT_LEDGER, private_key_path)
        builder.add_protocol(
            Path(ROOT_DIR, "packages", "fetchai", "protocols", "oef_search")
        )
        builder.add_connection(
            Path(ROOT_DIR, "packages", "fetchai", "connections", "local")
        )
        local_connection_id = OEFLocalConnection.connection_id
        builder.set_default_connection(local_connection_id)
        builder.add_skill(Path(CUR_PATH, "data", "dummy_skill"))
        aea = builder.build(connection_ids=[local_connection_id])
        local_connection = aea.resources.get_connection(local_connection_id)
        local_connection._local_node = node

        expected_message = DefaultMessage(
            dialogue_reference=("", ""),
            message_id=1,
            target=0,
            performative=DefaultMessage.Performative.BYTES,
            content=b"hello",
        )
        expected_message.to = aea.identity.address
        expected_message.sender = aea.identity.address
        envelope = Envelope(
            to=expected_message.to,
            sender=expected_message.sender,
            protocol_id=expected_message.protocol_id,
            message=expected_message,
        )

        with run_in_thread(aea.start, timeout=5, on_exit=aea.stop):
            wait_for_condition(lambda: aea.is_running, timeout=10)
            aea.outbox.put(envelope)

            dummy_skill_id = DUMMY_SKILL_PUBLIC_ID
            dummy_behaviour_name = "dummy"
            dummy_behaviour = aea.resources.get_behaviour(
                dummy_skill_id, dummy_behaviour_name
            )
            wait_for_condition(lambda: dummy_behaviour is not None, timeout=10)
            wait_for_condition(lambda: dummy_behaviour.nb_act_called > 0, timeout=10)

            # TODO the previous code caused an error:
            #      _pickle.PicklingError: Can't pickle <class 'tasks.DummyTask'>: import of module 'tasks' failed
            dummy_task = DummyTask()
            task_id = aea.enqueue_task(dummy_task)
            async_result = aea.get_task_result(task_id)
            expected_dummy_task = async_result.get(10.0)
            wait_for_condition(
                lambda: expected_dummy_task.nb_execute_called > 0, timeout=10
            )

            dummy_handler = aea.resources.get_handler(
                DefaultMessage.protocol_id, dummy_skill_id
            )
            dummy_handler_alt = aea.resources._handler_registry.fetch(
                (dummy_skill_id, "dummy")
            )
            wait_for_condition(lambda: dummy_handler == dummy_handler_alt, timeout=10)
            wait_for_condition(lambda: dummy_handler is not None, timeout=10)
            wait_for_condition(
                lambda: len(dummy_handler.handled_messages) == 1, timeout=10
            )
            wait_for_condition(
                lambda: dummy_handler.handled_messages[0] == expected_message,
                timeout=10,
            )


def test_initialize_aea_programmatically_build_resources():
    """Test that we can initialize the agent by building the resource object."""
    try:
        temp = tempfile.mkdtemp(prefix="test_aea_resources")
        with LocalNode() as node:
            agent_name = "MyAgent"
            private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
            wallet = Wallet({DEFAULT_LEDGER: private_key_path})
            identity = Identity(agent_name, address=wallet.addresses[DEFAULT_LEDGER])
            connection = _make_local_connection(agent_name, node)

            resources = Resources()
            aea = AEA(
                identity,
                wallet,
                resources=resources,
                default_connection=connection.public_id,
            )

            default_protocol = Protocol.from_dir(
                str(Path("packages", "fetchai", "protocols", "default"))
            )
            resources.add_protocol(default_protocol)
            resources.add_connection(connection)

            error_skill = Skill.from_dir(
                str(Path("packages", "fetchai", "skills", "error")),
                agent_context=aea.context,
            )
            dummy_skill = Skill.from_dir(
                str(Path(CUR_PATH, "data", "dummy_skill")), agent_context=aea.context
            )
            resources.add_skill(dummy_skill)
            resources.add_skill(error_skill)

            default_protocol_id = DefaultMessage.protocol_id

            expected_message = DefaultMessage(
                dialogue_reference=("", ""),
                message_id=1,
                target=0,
                performative=DefaultMessage.Performative.BYTES,
                content=b"hello",
            )
            expected_message.to = agent_name
            expected_message.sender = agent_name

            with run_in_thread(aea.start, timeout=5, on_exit=aea.stop):
                wait_for_condition(lambda: aea.is_running, timeout=10)
                aea.outbox.put(
                    Envelope(
                        to=agent_name,
                        sender=agent_name,
                        protocol_id=default_protocol_id,
                        message=expected_message,
                    )
                )

                dummy_skill_id = DUMMY_SKILL_PUBLIC_ID
                dummy_behaviour_name = "dummy"
                dummy_behaviour = aea.resources.get_behaviour(
                    dummy_skill_id, dummy_behaviour_name
                )
                wait_for_condition(lambda: dummy_behaviour is not None, timeout=10)
                wait_for_condition(
                    lambda: dummy_behaviour.nb_act_called > 0, timeout=10
                )

                dummy_task = DummyTask()
                task_id = aea.enqueue_task(dummy_task)
                async_result = aea.get_task_result(task_id)
                expected_dummy_task = async_result.get(10.0)
                wait_for_condition(
                    lambda: expected_dummy_task.nb_execute_called > 0, timeout=10
                )
                dummy_handler_name = "dummy"
                dummy_handler = aea.resources._handler_registry.fetch(
                    (dummy_skill_id, dummy_handler_name)
                )
                dummy_handler_alt = aea.resources.get_handler(
                    DefaultMessage.protocol_id, dummy_skill_id
                )
                wait_for_condition(
                    lambda: dummy_handler == dummy_handler_alt, timeout=10
                )
                wait_for_condition(lambda: dummy_handler is not None, timeout=10)
                wait_for_condition(
                    lambda: len(dummy_handler.handled_messages) == 1, timeout=10
                )
                wait_for_condition(
                    lambda: dummy_handler.handled_messages[0] == expected_message,
                    timeout=10,
                )
    finally:
        Path(temp).rmdir()


def test_add_behaviour_dynamically():
    """Test that we can add a behaviour dynamically."""
    agent_name = "MyAgent"
    private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
    wallet = Wallet({DEFAULT_LEDGER: private_key_path})
    resources = Resources()
    identity = Identity(agent_name, address=wallet.addresses[DEFAULT_LEDGER])
    connection = _make_local_connection(identity.address, LocalNode())
    agent = AEA(identity, wallet, resources, default_connection=connection.public_id,)
    resources.add_connection(connection)
    resources.add_component(
        Skill.from_dir(
            Path(CUR_PATH, "data", "dummy_skill"), agent_context=agent.context
        )
    )
    for skill in resources.get_all_skills():
        skill.skill_context.set_agent_context(agent.context)

    with run_in_thread(agent.start, timeout=5, on_exit=agent.stop):
        wait_for_condition(lambda: agent.is_running, timeout=10)

        dummy_skill_id = DUMMY_SKILL_PUBLIC_ID
        dummy_skill = agent.resources.get_skill(dummy_skill_id)

        wait_for_condition(lambda: dummy_skill is not None, timeout=10)

        new_behaviour = DummyBehaviour(
            name="dummy2", skill_context=dummy_skill.skill_context
        )
        dummy_skill.skill_context.new_behaviours.put(new_behaviour)

        wait_for_condition(lambda: new_behaviour.nb_act_called > 0, timeout=10)
        wait_for_condition(
            lambda: len(agent.resources.get_behaviours(dummy_skill_id)) == 2, timeout=10
        )


def test_error_handler_is_not_set():
    """Test stop on no error handler presents."""
    agent_name = "my_agent"
    private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
    wallet = Wallet({DEFAULT_LEDGER: private_key_path})
    identity = Identity(agent_name, address=wallet.addresses[DEFAULT_LEDGER])
    resources = Resources()
    context_namespace = {"key1": 1, "key2": 2}
    agent = AEA(identity, wallet, resources, **context_namespace)

    msg = DefaultMessage(
        dialogue_reference=("", ""),
        message_id=1,
        target=0,
        performative=DefaultMessage.Performative.BYTES,
        content=b"hello",
    )
    msg.to = agent.identity.address
    envelope = Envelope(
        to=agent.identity.address,
        sender=agent.identity.address,
        protocol_id=DefaultMessage.protocol_id,
        message=msg,
    )

    with pytest.raises(_StopRuntime):
        agent.handle_envelope(envelope)


def test_no_handlers_registered():
    """Test no handlers are registered for message processing."""
    agent_name = "MyAgent"
    builder = AEABuilder()
    private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
    builder.set_name(agent_name)
    builder.add_private_key(DEFAULT_LEDGER, private_key_path)
    aea = builder.build()

    with patch.object(
        aea._get_error_handler().context._logger, "warning"
    ) as mock_logger:
        msg = DefaultMessage(
            dialogue_reference=("", ""),
            message_id=1,
            target=0,
            performative=DefaultMessage.Performative.BYTES,
            content=b"hello",
        )
        msg.to = aea.identity.address
        envelope = Envelope(
            to=aea.identity.address,
            sender=aea.identity.address,
            protocol_id=DefaultMessage.protocol_id,
            message=msg,
        )
        with patch.object(
            aea.filter, "get_active_handlers", return_value=[]
        ), patch.object(
            aea.runtime.multiplexer, "put",
        ):
            aea.handle_envelope(envelope)
        mock_logger.assert_any_call(
            f"Cannot handle envelope: no active handler registered for the protocol_id='{DefaultMessage.protocol_id}'."
        )


class TestContextNamespace:
    """Test that the keyword arguments to AEA constructor can be accessible from the skill context."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        agent_name = "my_agent"
        private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
        wallet = Wallet({DEFAULT_LEDGER: private_key_path})
        identity = Identity(agent_name, address=wallet.addresses[DEFAULT_LEDGER])
        connection = _make_local_connection(identity.address, LocalNode())
        resources = Resources()
        cls.context_namespace = {"key1": 1, "key2": 2}
        cls.agent = AEA(identity, wallet, resources, **cls.context_namespace)

        resources.add_connection(connection)
        resources.add_component(
            Skill.from_dir(
                Path(CUR_PATH, "data", "dummy_skill"), agent_context=cls.agent.context
            )
        )
        for skill in resources.get_all_skills():
            skill.skill_context.set_agent_context(cls.agent.context)

    def test_access_context_namespace(self):
        """Test that we can access the context namespace."""
        assert self.agent.context.namespace.key1 == 1
        assert self.agent.context.namespace.key2 == 2

        for skill in self.agent.resources.get_all_skills():
            assert skill.skill_context.namespace.key1 == 1
            assert skill.skill_context.namespace.key2 == 2


def test_start_stop_and_start_stop_again():
    """Tests AEA can be started/stopped twice."""
    agent_name = "MyAgent"
    private_key_path = os.path.join(CUR_PATH, "data", DEFAULT_PRIVATE_KEY_FILE)
    builder = AEABuilder()
    builder.set_name(agent_name)
    builder.add_private_key(DEFAULT_LEDGER, private_key_path)
    builder.add_skill(Path(CUR_PATH, "data", "dummy_skill"))
    agent = builder.build()

    with run_in_thread(agent.start, timeout=20):
        wait_for_condition(lambda: agent.is_running, timeout=10)
        behaviour = agent.resources.get_behaviour(DUMMY_SKILL_PUBLIC_ID, "dummy")

        time.sleep(1)
        wait_for_condition(lambda: behaviour.nb_act_called > 0, timeout=5)
        agent.stop()
        wait_for_condition(lambda: agent.is_stopped, timeout=10)

    behaviour.nb_act_called = 0

    time.sleep(2)
    assert behaviour.nb_act_called == 0

    with run_in_thread(agent.start, timeout=20):
        wait_for_condition(lambda: agent.is_running, timeout=10)

        time.sleep(1)
        wait_for_condition(lambda: behaviour.nb_act_called > 0, timeout=5)
        agent.stop()
        wait_for_condition(lambda: agent.is_stopped, timeout=10)


class ExpectedExcepton(Exception):
    """Exception for testing."""


class TestAeaExceptionPolicy:
    """Tests for exception policies."""

    @staticmethod
    def raise_exception(*args, **kwargs) -> None:
        """Raise exception for tests."""
        raise ExpectedExcepton("we wait it!")

    def setup(self) -> None:
        """Set test cae instance."""
        agent_name = "MyAgent"

        builder = AEABuilder()
        builder.set_name(agent_name)
        builder.add_private_key(DEFAULT_LEDGER, FETCHAI_PRIVATE_KEY_PATH)

        self.handler_called = 0

        def handler_func(*args, **kwargs):
            self.handler_called += 1

        skill_context = SkillContext()
        handler_cls = make_handler_cls_from_funcion(handler_func)
        behaviour_cls = make_behaviour_cls_from_funcion(handler_func)

        self.handler = handler_cls(name="handler1", skill_context=skill_context)
        self.behaviour = behaviour_cls(name="behaviour1", skill_context=skill_context)

        test_skill = Skill(
            SkillConfig(name="test_skill", author="fetchai"),
            skill_context=skill_context,
            handlers={"handler": self.handler},
            behaviours={"behaviour": self.behaviour},
        )
        skill_context._skill = test_skill  # weird hack

        builder.add_component_instance(test_skill)
        self.aea = builder.build()
        self.aea_tool = AeaTool(self.aea)

    def test_no_exceptions(self) -> None:
        """Test act and handle works if no exception raised."""
        t = Thread(target=self.aea.start)
        t.start()

        self.aea_tool.put_inbox(self.aea_tool.dummy_envelope())
        time.sleep(1)
        assert self.handler_called >= 2

    def test_handle_propagate(self) -> None:
        """Test propagate policy on message handle."""
        self.aea._skills_exception_policy = ExceptionPolicyEnum.propagate
        self.handler.handle = self.raise_exception  # type: ignore # cause error: Cannot assign to a method
        self.aea_tool.put_inbox(self.aea_tool.dummy_envelope())

        with pytest.raises(ExpectedExcepton):
            self.aea.start()

        assert not self.aea.is_running

    def test_handle_stop_and_exit(self) -> None:
        """Test stop and exit policy on message handle."""
        self.aea._skills_exception_policy = ExceptionPolicyEnum.stop_and_exit
        self.handler.handle = self.raise_exception  # type: ignore # cause error: Cannot assign to a method
        self.aea_tool.put_inbox(self.aea_tool.dummy_envelope())

        with pytest.raises(
            AEAException, match=r"AEA was terminated cause exception .*"
        ):
            self.aea.start()

        assert not self.aea.is_running

    def test_handle_just_log(self) -> None:
        """Test just log policy on message handle."""
        self.aea._skills_exception_policy = ExceptionPolicyEnum.just_log
        self.handler.handle = self.raise_exception  # type: ignore # cause error: Cannot assign to a method

        with patch.object(self.aea._logger, "exception") as patched:
            t = Thread(target=self.aea.start)
            t.start()
            self.aea_tool.put_inbox(self.aea_tool.dummy_envelope())
            self.aea_tool.put_inbox(self.aea_tool.dummy_envelope())
            time.sleep(1)
        assert self.aea.is_running
        assert patched.call_count == 2

    def test_act_propagate(self) -> None:
        """Test propagate policy on behaviour act."""
        self.aea._skills_exception_policy = ExceptionPolicyEnum.propagate
        self.behaviour.act = self.raise_exception  # type: ignore # cause error: Cannot assign to a method

        with pytest.raises(ExpectedExcepton):
            self.aea.start()

        assert self.aea.runtime.state == RuntimeStates.error

    def test_act_stop_and_exit(self) -> None:
        """Test stop and exit policy on behaviour act."""
        self.aea._skills_exception_policy = ExceptionPolicyEnum.stop_and_exit
        self.behaviour.act = self.raise_exception  # type: ignore # cause error: Cannot assign to a method

        with pytest.raises(
            AEAException, match=r"AEA was terminated cause exception .*"
        ):
            self.aea.start()

        assert not self.aea.is_running

    def test_act_just_log(self) -> None:
        """Test just log policy on behaviour act."""
        self.aea._skills_exception_policy = ExceptionPolicyEnum.just_log
        self.behaviour.act = self.raise_exception  # type: ignore # cause error: Cannot assign to a method

        with patch.object(self.aea.logger, "exception") as patched:
            t = Thread(target=self.aea.start)
            t.start()

            time.sleep(1)
        assert self.aea.is_running
        assert patched.call_count > 1

    def test_act_bad_policy(self) -> None:
        """Test propagate policy on behaviour act."""
        self.aea._skills_exception_policy = "non exists policy"  # type: ignore
        self.behaviour.act = self.raise_exception  # type: ignore # cause error: Cannot assign to a method

        with pytest.raises(AEAException, match=r"Unsupported exception policy.*"):
            self.aea.start()

        assert not self.aea.is_running

    def teardown(self) -> None:
        """Stop AEA if not stopped."""
        self.aea.stop()


def sleep_a_bit(sleep_time: float = 0.1, num_of_sleeps: int = 1) -> None:
    """Sleep num_of_sleeps time for sleep_time.

    :param sleep_time: time to sleep.
    :param  num_of_sleeps: how many time sleep for sleep_time.

    :return: None
    """
    for _ in range(num_of_sleeps):
        time.sleep(sleep_time)


class BaseTimeExecutionCase(TestCase):
    """Base Test case for code execute timeout."""

    BASE_TIMEOUT = 0.35

    @classmethod
    def setUpClass(cls) -> None:
        """Set up."""
        if cls is BaseTimeExecutionCase:
            raise unittest.SkipTest("Skip BaseTest tests, it's a base class")

    def tearDown(self) -> None:
        """Tear down."""
        self.aea_tool.teardown()
        self.aea_tool.aea.runtime.main_loop._teardown()

    def prepare(self, function: Callable) -> None:
        """Prepare aea_tool for testing.

        :param function: function be called on react handle or/and Behaviour.act
        :return: None
        """
        agent_name = "MyAgent"

        builder = AEABuilder()
        builder.set_name(agent_name)
        builder.add_private_key(DEFAULT_LEDGER, FETCHAI_PRIVATE_KEY_PATH)

        self.function_finished = False

        def handler_func(*args, **kwargs):
            function()
            self.function_finished = True

        skill_context = SkillContext()
        handler_cls = make_handler_cls_from_funcion(handler_func)

        behaviour_cls = make_behaviour_cls_from_funcion(handler_func)
        self.behaviour = behaviour_cls(name="behaviour1", skill_context=skill_context)
        test_skill = Skill(
            SkillConfig(name="test_skill", author="fetchai"),
            skill_context=skill_context,
            handlers={
                "handler1": handler_cls(name="handler1", skill_context=skill_context)
            },
            behaviours={"behaviour1": self.behaviour},
        )
        skill_context._skill = test_skill  # weird hack

        builder.add_component_instance(test_skill)
        aea = builder.build()
        self.aea_tool = AeaTool(aea)
        self.envelope = AeaTool.dummy_envelope()
        self.aea_tool.aea.runtime.main_loop._setup()

    def test_long_handler_cancelled_by_timeout(self):
        """Test long function terminated by timeout."""
        num_sleeps = 10
        sleep_time = self.BASE_TIMEOUT
        function_sleep_time = num_sleeps * sleep_time
        execution_timeout = self.BASE_TIMEOUT * 2
        assert execution_timeout < function_sleep_time

        self.prepare(lambda: sleep_a_bit(sleep_time, num_sleeps))
        self.aea_tool.set_execution_timeout(execution_timeout)

        with timeit_context() as timeit:
            self.aea_action()

        assert execution_timeout <= timeit.time_passed <= function_sleep_time
        assert not self.function_finished

    def test_short_handler_not_cancelled_by_timeout(self):
        """Test short function NOT terminated by timeout."""
        num_sleeps = 1
        sleep_time = self.BASE_TIMEOUT
        function_sleep_time = num_sleeps * sleep_time
        execution_timeout = self.BASE_TIMEOUT * 2

        assert function_sleep_time <= execution_timeout

        self.prepare(lambda: sleep_a_bit(sleep_time, num_sleeps))
        self.aea_tool.set_execution_timeout(execution_timeout)
        self.aea_tool.setup()

        with timeit_context() as timeit:
            self.aea_action()

        assert function_sleep_time <= timeit.time_passed <= execution_timeout
        assert self.function_finished

    def test_no_timeout(self):
        """Test function NOT terminated by timeout cause timeout == 0."""
        num_sleeps = 1
        sleep_time = self.BASE_TIMEOUT
        function_sleep_time = num_sleeps * sleep_time
        execution_timeout = 0

        self.prepare(lambda: sleep_a_bit(sleep_time, num_sleeps))
        self.aea_tool.set_execution_timeout(execution_timeout)
        self.aea_tool.setup()

        with timeit_context() as timeit:
            self.aea_action()

        assert function_sleep_time <= timeit.time_passed
        assert self.function_finished


class HandleTimeoutExecutionCase(BaseTimeExecutionCase):
    """Test handle envelope timeout."""

    def aea_action(self):
        """Spin react on AEA."""
        self.aea_tool.aea.runtime.main_loop._execution_control(
            self.aea_tool.handle_envelope, [self.envelope]
        )


class ActTimeoutExecutionCase(BaseTimeExecutionCase):
    """Test act timeout."""

    def aea_action(self):
        """Spin act on AEA."""
        self.aea_tool.aea.runtime.main_loop._execution_control(
            self.behaviour.act_wrapper
        )
