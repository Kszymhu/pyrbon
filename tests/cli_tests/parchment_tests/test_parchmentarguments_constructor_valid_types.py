from pyrbon.cli.parchment_arguments import ParchmentArguments

'''
ParchmentArguments constructor should accept valid argument types.
'''

def test_constructor_accepts_a_integer_b_float():
    dummy_a = 1
    dummy_b = 1.1

    parchment_arguments = ParchmentArguments(dummy_a, dummy_b)

    assert parchment_arguments.dummy_a == dummy_a
    assert parchment_arguments.dummy_b == dummy_b


def test_constructor_accepts_a_integer_b_integer() -> None:
    dummy_a = 1
    dummy_b = 1

    parchment_arguments = ParchmentArguments(dummy_a, dummy_b)

    assert parchment_arguments.dummy_a == dummy_a
    assert parchment_arguments.dummy_b == dummy_b
