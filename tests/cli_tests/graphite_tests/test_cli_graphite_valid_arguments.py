from pyrbon.cli.create_parser import create_parser

'''
CLI should accept:
    - integers for A
    - integers and floats for B
'''


def test_cli_accepts_a_integer_b_float() -> None:
    dummy_a = 1
    dummy_b = 1.1

    arguments = ['graphite', '-a', str(dummy_a), '-b', str(dummy_b)]

    parser = create_parser()

    parsed_arguments = parser.parse_args(arguments)

    assert parsed_arguments.dummy_a == dummy_a
    assert parsed_arguments.dummy_b == dummy_b


def test_cli_accepts_a_integer_b_integer() -> None:
    dummy_a = 1
    dummy_b = 1

    arguments = ['graphite', '-a', str(dummy_a), '-b', str(dummy_b)]

    parser = create_parser()

    parsed_arguments = parser.parse_args(arguments)

    assert parsed_arguments.dummy_a == dummy_a
    assert parsed_arguments.dummy_b == dummy_b
