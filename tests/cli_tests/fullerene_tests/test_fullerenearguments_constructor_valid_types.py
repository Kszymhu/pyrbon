from pyrbon.cli.fullerene_arguments import FullereneArguments

'''
FullereneArguments constructor should accept valid argument types.
'''

def test_constructor_accepts_a_integer_b_float():
    dummy_a = 1
    dummy_b = 1.1

    fullerene_arguments = FullereneArguments(dummy_a, dummy_b)

    assert fullerene_arguments.dummy_a == dummy_a
    assert fullerene_arguments.dummy_b == dummy_b


def test_constructor_accepts_a_integer_b_integer() -> None:
    dummy_a = 1
    dummy_b = 1

    fullerene_arguments = FullereneArguments(dummy_a, dummy_b)

    assert fullerene_arguments.dummy_a == dummy_a
    assert fullerene_arguments.dummy_b == dummy_b
