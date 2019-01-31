CodeSync
========

CodeSync will Sync your git folders to or from a local directory and a 
remote machine.

## How To Install
    pip install codesync

## Options

##### positional arguments:
      -p PROJECT, --project PROJECT
                            The name of your local git project, stored under your
                            default path. Default: /Users/nmagnezi/git/<project>

      -d {to,from}, --direction {to,from}
                            Sync Direction
    
      -i IP, --ip IP        IP Address for SSH connection


##### optional arguments:
      -f FOLDER, --folder FOLDER
                            Remote git folder. Default: /opt/stack/
    
      -u USER, --user USER  Username for ssh connection. Default: stack

## Usage Example

    codesync -p octavia -d to -i 10.35.6.107 -f /my/path -u blah

## How does it work?

These are steps performed by CodeSync:

1. Validate your node has rsync installed.
2. Use rsync to sync the delta between source and destination.
