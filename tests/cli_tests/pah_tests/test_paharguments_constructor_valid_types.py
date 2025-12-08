from pyrbon.cli.pah_arguments import PahArguments

'''
PahArguments constructor should accept valid argument types.
'''

def test_constructor_accepts_a_integer_b_float():
    dummy_a = 1
    dummy_b = 1.1

    parchment_arguments = PahArguments(dummy_a, dummy_b)

    assert parchment_arguments.dummy_a == dummy_a
    assert parchment_arguments.dummy_b == dummy_b


def test_constructor_accepts_a_integer_b_integer() -> None:
    dummy_a = 1
    dummy_b = 1

    parchment_arguments = PahArguments(dummy_a, dummy_b)

    assert parchment_arguments.dummy_a == dummy_a
    assert parchment_arguments.dummy_b == dummy_b
