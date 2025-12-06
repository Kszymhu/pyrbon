import pytest
from pyrbon.cli.create_parser import create_parser

'''
CLI should reject:
    - floats and strings for A
    - strings for B
'''


def test_cli_rejects_a_float_b_float() -> None:
    dummy_a = 1.1
    dummy_b = 1.1

    arguments = ['fullerene', '-a', str(dummy_a), '-b', str(dummy_b)]

    parser = create_parser()

    with pytest.raises(SystemExit):
        parser.parse_args(arguments)


def test_cli_rejects_a_str_b_float() -> None:
    dummy_a = 'shrimp'
    dummy_b = 1.1

    arguments = ['fullerene', '-a', str(dummy_a), '-b', str(dummy_b)]

    parser = create_parser()

    with pytest.raises(SystemExit):
        parser.parse_args(arguments)


def test_cli_rejects_a_integer_b_str() -> None:
    dummy_a = 1
    dummy_b = 'shrimp'

    arguments = ['fullerene', '-a', str(dummy_a), '-b', str(dummy_b)]

    parser = create_parser()

    with pytest.raises(SystemExit):
        parser.parse_args(arguments)
