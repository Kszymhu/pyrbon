import sys

from pyrbon.cli.create_parser import create_parser
from pyrbon.cli.get_command_arguments import get_command_arguments


def main() -> None:
    parser = create_parser()
    parsed_arguments = parser.parse_args()
    command_arguments = get_command_arguments(parsed_arguments)
    
    sys.exit(0)


if __name__ == '__main__':
    main()