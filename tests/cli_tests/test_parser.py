import pytest

from pyrbon.cli.create_parser import create_parser

def test_create_parser_works() -> None:
    create_parser()


def test_parser_throws_error_no_generator() -> None:
    parser = create_parser()

    with pytest.raises(SystemExit):
        parser.parse_args([])