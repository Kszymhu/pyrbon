import pytest

from pyrbon.cli.create_parser import create_parser

'''
CLI should throw errors if required arguments and/or their values are missing.
'''


def test_cli_rejects_missing_arguments() -> None:
    parser = create_parser()

    arguments = ['pah']

    with pytest.raises(SystemExit):
        parser.parse_args(arguments)


def test_cli_rejects_missing_values() -> None:
    parser = create_parser()

    arguments = ['pah', '-a', '-b']

    with pytest.raises(SystemExit):
        parser.parse_args(arguments)
