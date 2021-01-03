import logging
import sys

import args_parser
import constants
import helpers

LOG = logging.getLogger(__name__)


def main(args):
    LOG.debug("CodeSync Starts.")
    try:
        helpers.startup_validations(args)
    except RuntimeError:
        return constants.EXIT_ERROR


if __name__ == '__main__':
    cmd_line_args = args_parser.process_args()
    helpers.configure_logger(cmd_line_args.debug)
    sys.exit(main(cmd_line_args))
