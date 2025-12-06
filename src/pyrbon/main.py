import sys

from pyrbon.cli.create_parser import create_parser
from pyrbon.cli.get_command_arguments import get_command_arguments

from pyrbon.cli.diamond_arguments import DiamondArguments
from pyrbon.cli.fullerene_arguments import FullereneArguments
from pyrbon.cli.graphene_arguments import GrapheneArguments
from pyrbon.cli.graphite_arguments import GraphiteArguments
from pyrbon.cli.mwcnt_arguments import MwcntArguments
from pyrbon.cli.parchment_arguments import ParchmentArguments
from pyrbon.cli.swcnt_arguments import SwcntArguments


def main() -> None:
    parser = create_parser()
    parsed_arguments = parser.parse_args()
    command_arguments = get_command_arguments(parsed_arguments)

    if isinstance(command_arguments, DiamondArguments):
        print('Diamond generator was chosen. Too bad it\'s not implemented yet.')
    elif isinstance(command_arguments, FullereneArguments):
        print('Fullerene generator was chosen. Too bad it\'s not implemented yet.')
    elif isinstance(command_arguments, GrapheneArguments):
        print('Graphene generator was chosen. Too bad it\'s not implemented yet. But it will be soon :3')
    elif isinstance(command_arguments, GraphiteArguments):
        print('Graphite generator was chosen. Too bad it\'s not implemented yet.')
    elif isinstance(command_arguments, MwcntArguments):
        print('MWCNT generator was chosen. Too bad it\'s not implemented yet.')
    elif isinstance(command_arguments, ParchmentArguments):
        print('Parchment MWCNT generator was chosen. Too bad it\'s not implemented yet.')
    elif isinstance(command_arguments, SwcntArguments):
        print('SWCNT generator was chosen. Too bad it\'s not implemented yet.')

    sys.exit(0)


if __name__ == '__main__':
    main()