from pyrbon.cli.graphene_arguments import GrapheneArguments

'''
GrapheneArguments constructor should accept valid argument types.
'''

def test_constructor_accepts_a_integer_b_float():
    dummy_a = 1
    dummy_b = 1.1

    graphene_arguments = GrapheneArguments(dummy_a, dummy_b)

    assert graphene_arguments.dummy_a == dummy_a
    assert graphene_arguments.dummy_b == dummy_b


def test_constructor_accepts_a_integer_b_integer() -> None:
    dummy_a = 1
    dummy_b = 1

    graphene_arguments = GrapheneArguments(dummy_a, dummy_b)

    assert graphene_arguments.dummy_a == dummy_a
    assert graphene_arguments.dummy_b == dummy_b
