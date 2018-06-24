#!/usr/bin/env python

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
from os import path
import subprocess

import constants
import helpers


def process_args():
    parser = argparse.ArgumentParser(
        description='Sync git folders to or from a local directory and a'
                    'remote machine')
    parser.add_argument(
        '-p', '--project',
        required=True,
        help='Local git project, stored under your default path')
    parser.add_argument(
        '-f', '--folder',
        required=False,
        default=constants.REMOTE_PATH,
        help='Remote git folder')
    parser.add_argument(
        '-d', '--direction',
        required=True,
        choices=['to', 'from'],
        help='Sync Direction')
    parser.add_argument(
        '-u', '--user',
        required=False,
        default=constants.SSH_USER,
        help='Username for ssh connection')
    parser.add_argument(
        '-i', '--ip',
        required=False,
        default=constants.SSH_USER,
        help='IP Address for ssh connection')
    return parser.parse_args()


def main():
    rsync = helpers.get_rsync_path()
    args = process_args()
    local = path.join(helpers.get_git_directory_path(), args.project)
    remote = "".join([args.user, '@', args.ip, ':', args.folder])
    if args.direction == 'to':
        cmd = " ".join([rsync, constants.RSYNC_ARGS, local, remote])
    else:
        cmd = " ".join([rsync, constants.RSYNC_ARGS, remote, local])

    print "Executing: " + "".join(cmd)
    subprocess.call(cmd.split())


if __name__ == '__main__':
    main()
