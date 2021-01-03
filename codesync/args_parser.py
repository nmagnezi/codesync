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

import argparse
import getpass
import os

import constants


def process_args():
    parser = argparse.ArgumentParser(
        prog='codesync',
        add_help=True,
        description='Sync code folders to or from a local directory and a '
                    'remote machine.',
    )
    positional_args = parser.add_argument_group('positional arguments')
    positional_args.add_argument(
        '-i', '--ip',
        required=True,
        help='IP Address for ssh connection'
    )
    direction = parser.add_mutually_exclusive_group()
    direction.add_argument(
        '-t', '--to',
        help='Sync to destination (default sync direction)',
        nargs='?'
    )
    direction.add_argument(
        '-f', '--from',
        help='Sync from destination',
        nargs='?'
    )
    parser.add_argument(
        '-lf', '--local-folder',
        required=False,
        default=os.getcwd(),
        help='Local code folder. Defaults to current shell path:'
             ' {}'.format(os.getcwd())
    )
    parser.add_argument(
        '-rf', '--remote-folder',
        required=False,
        default=os.getcwd(),
        help='Remote code folder. Defaults to current local shell path:'
             ' {}'.format(os.getcwd())
    )
    parser.add_argument(
        '-p', '--project',
        required=False,
        help='Overrides --local-folder. The name of your local project, '
             'stored under a default path (environment variable: '
             '{}). Example: {}{}'
             .format(constants.CODESYNC_PROJECTS_DIR_ENV,
                     os.path.expanduser("~"),
                     '/git/<myproject>'
                     )
    )
    parser.add_argument(
        '-u', '--user',
        required=False,
        default=getpass.getuser(),
        help='Username for ssh connection. '
             'Defaults to current shell user: {}'.format( getpass.getuser())
    )
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        required=False,
        default=False,
        help='Enable Debug mode.',
    )
    return parser.parse_args()
