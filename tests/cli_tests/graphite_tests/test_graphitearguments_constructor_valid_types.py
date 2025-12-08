from pyrbon.cli.graphite_arguments import GraphiteArguments

'''
GraphiteArguments constructor should accept valid argument types.
'''

def test_constructor_accepts_a_integer_b_float():
    dummy_a = 1
    dummy_b = 1.1

    graphite_arguments = GraphiteArguments(dummy_a, dummy_b)

    assert graphite_arguments.dummy_a == dummy_a
    assert graphite_arguments.dummy_b == dummy_b


def test_constructor_accepts_a_integer_b_integer() -> None:
    dummy_a = 1
    dummy_b = 1

    graphite_arguments = GraphiteArguments(dummy_a, dummy_b)

    assert graphite_arguments.dummy_a == dummy_a
    assert graphite_arguments.dummy_b == dummy_b
