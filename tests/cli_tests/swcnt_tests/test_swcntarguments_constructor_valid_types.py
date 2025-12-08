from pyrbon.cli.swcnt_arguments import SwcntArguments

'''
SwcntArguments constructor should accept valid argument types.
'''

def test_constructor_accepts_a_integer_b_float():
    dummy_a = 1
    dummy_b = 1.1

    swcnt_arguments = SwcntArguments(dummy_a, dummy_b)

    assert swcnt_arguments.dummy_a == dummy_a
    assert swcnt_arguments.dummy_b == dummy_b


def test_constructor_accepts_a_integer_b_integer() -> None:
    dummy_a = 1
    dummy_b = 1

    swcnt_arguments = SwcntArguments(dummy_a, dummy_b)

    assert swcnt_arguments.dummy_a == dummy_a
    assert swcnt_arguments.dummy_b == dummy_b
