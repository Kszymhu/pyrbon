import pytest

from pyrbon.cli.mwcnt_arguments import MwcntArguments

'''
MwcntArguments constructor should reject invalid argument values.
'''

def test_constructor_rejects_a_invalid_b_valid():
    dummy_a = 2137
    dummy_b = 1.1

    with pytest.raises(ValueError):
        MwcntArguments(dummy_a, dummy_b)


def test_constructor_rejects_a_valid_b_invalid() -> None:
    dummy_a = 1
    dummy_b = 2.137

    with pytest.raises(ValueError):
        MwcntArguments(dummy_a, dummy_b)
