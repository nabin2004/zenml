#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""CLI functionality to interact with artifacts."""
import os

import click

from zenml.cli.cli import TagGroup, cli
from zenml.constants import ENV_ZENML_HUB_URL
from zenml.enums import CliCategories
from zenml.logger import get_logger

HUB_URL = os.getenv(ENV_ZENML_HUB_URL)

logger = get_logger(__name__)

@cli.group(cls=TagGroup, tag=CliCategories.HUB)
def hub() -> None:
    """List or delete artifacts."""

@hub.command()
@click.argument("plugin_name", type=str, required=True)
def install(
    plugin_name: str
):
    """Install a plugin from the hub."""

    # GET on /plugins/{plugin_id} to fetch the wheel url

    # pip install the wheel