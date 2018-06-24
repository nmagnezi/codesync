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

from distutils import spawn
from os import path


import constants


def get_git_directory_path():
    home_dir = path.expanduser("~")
    return path.join(home_dir, constants.GIT_DIR)


def get_rsync_path():
    rsync = spawn.find_executable(constants.RSYNC_BINARY)
    if not rsync:
        raise RuntimeError('rsync is not installed, cannot continue. '
                           'Please install rsync and try again.')
    return rsync
