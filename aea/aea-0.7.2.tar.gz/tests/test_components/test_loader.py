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

"""This module contains tests for aea/components/loader.py"""
from unittest import mock

import pytest

from aea.components.loader import load_component_from_config
from aea.configurations.base import ProtocolConfig
from aea.exceptions import AEAPackageLoadingError
from aea.protocols.base import Protocol


@pytest.fixture(scope="module")
def component_configuration():
    """Return a component configuration."""
    return ProtocolConfig("a_protocol", "an_author", "0.1.0")


def test_component_loading_generic_exception(component_configuration):
    """Test 'load_component_from_config' method when a generic "Exception" occurs."""

    with mock.patch.object(
        Protocol, "from_config", side_effect=Exception("Generic exception")
    ):
        with pytest.raises(
            Exception, match="An error occurred while loading .*: Generic exception"
        ):
            load_component_from_config(component_configuration)


def test_component_loading_generic_module_not_found_error(component_configuration):
    """Test 'load_component_from_config' method when a generic "ModuleNotFoundError" occurs."""

    with mock.patch.object(
        Protocol,
        "from_config",
        side_effect=ModuleNotFoundError(
            "An error occurred while loading .*: Generic error"
        ),
    ):
        with pytest.raises(ModuleNotFoundError, match="Generic error"):
            load_component_from_config(component_configuration)


def test_component_loading_module_not_found_error_non_framework_package(
    component_configuration,
):
    """Test 'load_component_from_config' method when a "ModuleNotFoundError" occurs for a generic import path (non framework related."""
    with mock.patch.object(
        Protocol,
        "from_config",
        side_effect=ModuleNotFoundError("No module named 'generic.package'"),
    ):
        with pytest.raises(ModuleNotFoundError):
            load_component_from_config(component_configuration)


def test_component_loading_module_not_found_error_framework_package(
    component_configuration,
):
    """Test 'load_component_from_config' method when a "ModuleNotFoundError" occurs for a framework-related import (starts with 'packages') but for some reason it doesn't contain the author name."""
    with mock.patch.object(
        Protocol,
        "from_config",
        side_effect=ModuleNotFoundError("No module named 'packages'"),
    ):
        with pytest.raises(ModuleNotFoundError, match="No module named 'packages'"):
            load_component_from_config(component_configuration)


def test_component_loading_module_not_found_error_framework_package_with_wrong_author(
    component_configuration,
):
    """Test 'load_component_from_config' method when a "ModuleNotFoundError" occurs for a framework-related import (starts with 'packages') with wrong author."""
    with mock.patch.object(
        Protocol,
        "from_config",
        side_effect=ModuleNotFoundError("No module named 'packages.some_author'"),
    ):
        with pytest.raises(
            AEAPackageLoadingError,
            match="No module named packages.some_author; No AEA package found with author name 'some_author'",
        ):
            load_component_from_config(component_configuration)


def test_component_loading_module_not_found_error_framework_package_with_wrong_type(
    component_configuration,
):
    """Test 'load_component_from_config' method when a "ModuleNotFoundError" occurs for a framework-related import (starts with 'packages') with correct author but wrong type."""
    with mock.patch.object(
        Protocol,
        "from_config",
        side_effect=ModuleNotFoundError(
            "No module named 'packages.some_author.some_type'"
        ),
    ):
        with pytest.raises(
            AEAPackageLoadingError,
            match=r"No module named packages.some_author.some_type; 'some_type' is not a valid type name, choose one of \['protocols', 'connections', 'skills', 'contracts'\]",
        ):
            load_component_from_config(component_configuration)


def test_component_loading_module_not_found_error_framework_package_with_wrong_name(
    component_configuration,
):
    """Test 'load_component_from_config' method when a "ModuleNotFoundError" occurs for a framework-related import (starts with 'packages') with correct author and type but wrong name."""
    with mock.patch.object(
        Protocol,
        "from_config",
        side_effect=ModuleNotFoundError(
            "No module named 'packages.some_author.protocols.some_name'"
        ),
    ):
        with pytest.raises(
            AEAPackageLoadingError,
            match="No module named packages.some_author.protocols.some_name; No AEA package found with author name 'some_author', type 'protocols', name 'some_name'",
        ):
            load_component_from_config(component_configuration)


def test_component_loading_module_not_found_error_framework_package_with_wrong_suffix(
    component_configuration,
):
    """Test 'load_component_from_config' method when a "ModuleNotFoundError" occurs for a framework-related import (starts with 'packages') with correct author and type but wrong suffix."""
    with mock.patch.object(
        Protocol,
        "from_config",
        side_effect=ModuleNotFoundError(
            "No module named 'packages.some_author.protocols.some_name.some_subpackage'"
        ),
    ):
        with pytest.raises(
            AEAPackageLoadingError,
            match="No module named packages.some_author.protocols.some_name.some_subpackage; The package 'packages/some_author' of type 'protocols' exists, but cannot find module 'some_subpackage'",
        ):
            load_component_from_config(component_configuration)
