import pytest

from pyrbon.cli.graphene_arguments import GrapheneArguments

'''
GrapheneArguments constructor should reject invalid argument types.
'''

def test_constructor_rejects_a_float_b_float():
    dummy_a = 1.1
    dummy_b = 1.1

    with pytest.raises(TypeError):
        GrapheneArguments(dummy_a, dummy_b)


def test_constructor_rejects_a_str_b_float() -> None:
    dummy_a = 'shrimp'
    dummy_b = 1.1

    with pytest.raises(TypeError):
        GrapheneArguments(dummy_a, dummy_b)


def test_constructor_rejects_a_integer_b_str() -> None:
    dummy_a = 1
    dummy_b = 'shrimp'

    with pytest.raises(TypeError):
        GrapheneArguments(dummy_a, dummy_b)
