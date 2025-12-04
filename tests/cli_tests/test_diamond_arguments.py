import pytest

from pyrbon.cli.diamond_arguments import DiamondArguments

VALID_DUMMY_A: int = 1
INVALID_DUMMY_A: int = 2137

VALID_DUMMY_B: float = 1.2
INVALID_DUMMY_B: float = 2.137


def test_instantiation_accepts_valid_arguments():
    diamond_arguments = DiamondArguments(
        VALID_DUMMY_A,
        VALID_DUMMY_B
    )

    assert(diamond_arguments.dummy_a == VALID_DUMMY_A)
    assert(diamond_arguments.dummy_b == VALID_DUMMY_B)


def test_instantiation_rejects_invalid_dummy_a():
    with pytest.raises(ValueError):
        DiamondArguments(
            INVALID_DUMMY_A,
            VALID_DUMMY_B
        )


def test_instantiation_rejects_invalid_dummy_b():
    with pytest.raises(ValueError):
        DiamondArguments(
            VALID_DUMMY_A,
            INVALID_DUMMY_B
        )