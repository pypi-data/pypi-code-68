#!/usr/bin/env python3
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
"""
Check that every package has existing dependencies.

Run this script from the root of the project directory:

    python scripts/check_package_dependencies.py

"""
import pprint
import sys
from functools import partial
from itertools import chain
from pathlib import Path
from typing import Dict, List, Set

import yaml

from aea.configurations.base import PackageId, PackageType, PublicId


DEFAULT_CONFIG_FILE_PATHS = []  # type: List[Path]


class DependencyNotFound(Exception):
    """Custom exception for dependencies not found."""

    def __init__(
        self,
        configuration_file: Path,
        expected_deps: Set[PackageId],
        missing_dependencies: Set[PackageId],
        *args,
    ):
        """
        Initialize DependencyNotFound exception.

        :param configuration_file: path to the checked file.
        :param expected_dependencies: expected dependencies.
        :param missing_dependencies: missing dependencies.
        :param kwargs: super class args.
        """
        super().__init__(*args)
        self.configuration_file = configuration_file
        self.expected_dependencies = expected_deps
        self.missing_dependencies = missing_dependencies


def find_all_configuration_files():
    """Find all configuration files."""
    packages_dir = Path("packages")
    return list(chain(packages_dir.glob("*/*/*/*.yaml"), default_config_file_paths()))


def default_config_file_paths():
    """Get (generator) the default config file paths."""
    for item in DEFAULT_CONFIG_FILE_PATHS:
        yield item


def get_public_id_from_yaml(configuration_file: Path):
    """
    Get the public id from yaml.

    :param configuration_file: the path to the config yaml
    """
    data = unified_yaml_load(configuration_file)
    author = data["author"]
    # handle the case when it's a package or agent config file.
    name = data["name"] if "name" in data else data["agent_name"]
    version = data["version"]
    return PublicId(author, name, version)


def find_all_packages_ids() -> Set[PackageId]:
    """Find all packages ids."""
    package_ids: Set[PackageId] = set()
    for configuration_file in find_all_configuration_files():
        package_type = PackageType(configuration_file.parts[-3][:-1])
        package_public_id = get_public_id_from_yaml(configuration_file)
        package_id = PackageId(package_type, package_public_id)
        package_ids.add(package_id)

    return package_ids


def handle_dependency_not_found(e: DependencyNotFound):
    """Handle PackageIdNotFound errors."""
    sorted_expected = list(map(str, sorted(e.expected_dependencies)))
    sorted_missing = list(map(str, sorted(e.missing_dependencies)))
    print("=" * 50)
    print(f"Package {e.configuration_file}:")
    print(f"Expected: {pprint.pformat(sorted_expected)}")
    print(f"Missing: {pprint.pformat(sorted_missing)}")


def unified_yaml_load(configuration_file: Path) -> Dict:
    """
    Load YAML file, unified (both single- and multi-paged).

    :param configuration_file: the configuration file path.
    :return: the data.
    """
    package_type = configuration_file.parent.parent.name
    with configuration_file.open() as fp:
        if package_type != "agents":
            return yaml.safe_load(fp)
        # when it is an agent configuration file,
        # we are interested only in the first page of the YAML,
        # because the dependencies are contained only there.
        data = yaml.safe_load_all(fp)
        return list(data)[0]


def check_dependencies(configuration_file: Path, all_packages_ids: Set[PackageId]):
    """
    Check dependencies of configuration file.

    :param configuration_file: path to a package configuration file.
    :param all_packages_ids: all the package ids.
    :return: None
    """
    data = unified_yaml_load(configuration_file)

    def _add_package_type(package_type, public_id_str):
        return PackageId(package_type, PublicId.from_str(public_id_str))

    def _get_package_ids(package_type, public_ids):
        return set(map(partial(_add_package_type, package_type), public_ids))

    dependencies: Set[PackageId] = set.union(
        *[
            _get_package_ids(package_type, data.get(package_type.to_plural(), set()))
            for package_type in list(PackageType)
        ]
    )

    diff = dependencies.difference(all_packages_ids)
    if len(diff) > 0:
        raise DependencyNotFound(configuration_file, dependencies, diff)


if __name__ == "__main__":
    all_packages_ids_ = find_all_packages_ids()
    failed: bool = False
    for file in find_all_configuration_files():
        try:
            print("Processing " + str(file))
            check_dependencies(file, all_packages_ids_)
        except DependencyNotFound as e_:
            handle_dependency_not_found(e_)
            failed = True

    if failed:
        print("Failed!")
        sys.exit(1)
    else:
        print("OK!")
        sys.exit(0)
