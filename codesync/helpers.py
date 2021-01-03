# Copyright 2018 Nir Magnezi
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import logging

from distutils import spawn
from os import path

import constants

LOG = logging.getLogger(__name__)


def configure_logger(debug_mode):
    logging.basicConfig(
        level=logging.DEBUG if debug_mode is True else logging.INFO,
        format='%(asctime)s :: CodeSync :: %(levelname)s :: %(message)s'
    )


def startup_validations(args):
    errors = list()
    if not spawn.find_executable(constants.RSYNC_BINARY):
        errors.append(
            'rsync is not installed, cannot continue. '
            'Please install rsync and try again.'
        )
    if (args.project and os.environ.get(constants.CODESYNC_PROJECTS_DIR_ENV)
            is None):
        errors.append(
            f"Please set {constants.CODESYNC_PROJECTS_DIR_ENV} to use the "
            f"-p/--project option"
        )
    if not errors:
        return
    for err in errors:
        LOG.error(err)
    raise RuntimeError


def get_rsync_path():
    rsync = spawn.find_executable(constants.RSYNC_BINARY)
    if not rsync:
        raise RuntimeError()
    return rsync
