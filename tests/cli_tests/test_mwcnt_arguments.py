import pytest

from pyrbon.cli.mwcnt_arguments import MwcntArguments


def test_instantiation_accepts_valid_arguments():
    valid_dummy_a = 1
    valid_dummy_b = 1.2

    mwcnt_arguments = MwcntArguments(
        valid_dummy_a,
        valid_dummy_b
    )

    assert(mwcnt_arguments.dummy_a == valid_dummy_a)
    assert(mwcnt_arguments.dummy_b == valid_dummy_b)


def test_instantiation_rejects_invalid_dummy_a():
    invalid_dummy_a = 2137
    valid_dummy_b = 1.2

    with pytest.raises(ValueError):
        MwcntArguments(
            invalid_dummy_a,
            valid_dummy_b
        )


def test_instantiation_rejects_invalid_dummy_b():
    valid_dummy_a = 1
    invalid_dummy_b = 2.137

    with pytest.raises(ValueError):
        MwcntArguments(
            valid_dummy_a,
            invalid_dummy_b
        )