from pyrbon.cli.create_parser import create_parser

'''
CLI should accept named arguments regardless of:
    - their order
    - whether or not the names are short/long
'''


def test_cli_accepts_short_arguments() -> None:
    dummy_a = 1
    dummy_b = 1.1

    arguments = ['swcnt', '-a', str(dummy_a), '-b', str(dummy_b)]

    parser = create_parser()

    parsed_arguments = parser.parse_args(arguments)

    assert parsed_arguments.dummy_a == dummy_a
    assert parsed_arguments.dummy_b == dummy_b


def test_cli_accepts_long_arguments() -> None:
    dummy_a = 1
    dummy_b = 1.1

    arguments = ['swcnt', '--dummy_a', str(dummy_a), '--dummy_b', str(dummy_b)]

    parser = create_parser()

    parsed_arguments = parser.parse_args(arguments)

    assert parsed_arguments.dummy_a == dummy_a
    assert parsed_arguments.dummy_b == dummy_b   


def test_cli_accepts_reverse_order_short_arguments() -> None:
    dummy_a = 1
    dummy_b = 1.1

    arguments = ['swcnt', '-b', str(dummy_b), '-a', str(dummy_a)]

    parser = create_parser()

    parsed_arguments = parser.parse_args(arguments)

    assert parsed_arguments.dummy_a == dummy_a
    assert parsed_arguments.dummy_b == dummy_b


def test_cli_accepts_reverse_order_long_arguments() -> None:
    dummy_a = 1
    dummy_b = 1.1

    arguments = ['swcnt', '--dummy_b', str(dummy_b), '--dummy_a', str(dummy_a)]

    parser = create_parser()

    parsed_arguments = parser.parse_args(arguments)

    assert parsed_arguments.dummy_a == dummy_a
    assert parsed_arguments.dummy_b == dummy_b  
