from pyrbon.cli.mwcnt_arguments import MwcntArguments

'''
MwcntArguments constructor should accept valid argument types.
'''

def test_constructor_accepts_a_integer_b_float():
    dummy_a = 1
    dummy_b = 1.1

    mwcnt_arguments = MwcntArguments(dummy_a, dummy_b)

    assert mwcnt_arguments.dummy_a == dummy_a
    assert mwcnt_arguments.dummy_b == dummy_b


def test_constructor_accepts_a_integer_b_integer() -> None:
    dummy_a = 1
    dummy_b = 1

    mwcnt_arguments = MwcntArguments(dummy_a, dummy_b)

    assert mwcnt_arguments.dummy_a == dummy_a
    assert mwcnt_arguments.dummy_b == dummy_b
