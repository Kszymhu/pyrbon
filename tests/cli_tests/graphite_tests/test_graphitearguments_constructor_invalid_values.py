import pytest

from pyrbon.cli.graphite_arguments import GraphiteArguments

'''
GraphiteArguments constructor should reject invalid argument values.
'''

def test_constructor_rejects_a_invalid_b_valid():
    dummy_a = 2137
    dummy_b = 1.1

    with pytest.raises(ValueError):
        GraphiteArguments(dummy_a, dummy_b)


def test_constructor_rejects_a_valid_b_invalid() -> None:
    dummy_a = 1
    dummy_b = 2.137

    with pytest.raises(ValueError):
        GraphiteArguments(dummy_a, dummy_b)
