from pyrbon.cli.diamond_arguments import DiamondArguments

'''
DiamondArguments constructor should accept valid argument types.
'''

def test_constructor_accepts_a_integer_b_float():
    dummy_a = 1
    dummy_b = 1.1

    diamond_arguments = DiamondArguments(dummy_a, dummy_b)

    assert diamond_arguments.dummy_a == dummy_a
    assert diamond_arguments.dummy_b == dummy_b


def test_constructor_accepts_a_integer_b_integer() -> None:
    dummy_a = 1
    dummy_b = 1

    diamond_arguments = DiamondArguments(dummy_a, dummy_b)

    assert diamond_arguments.dummy_a == dummy_a
    assert diamond_arguments.dummy_b == dummy_b
