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

CODESYNC_PROJECTS_DIR_ENV = 'CODESYNC_PROJECTS_DIR'

EXIT_ERROR = 1
GIT_DIR = "git/"
REMOTE_PATH = "/opt/stack/"

SSH_USER = "stack"
RSYNC_BINARY = "rsync"

# Excludes list composed with the kind help of John Schwarz: https://github.com/jschwarz89
RSYNC_ARGS = ("-v -r --exclude=.tox --exclude=.idea --exclude=*.pyc "
              "--exclude=*.pyo --exclude=*~ --exclude=.*.swp --exclude=.*.swo "
              "-azh --progress --delete")
