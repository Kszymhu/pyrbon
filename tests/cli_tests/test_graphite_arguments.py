import pytest

from pyrbon.cli.graphite_arguments import GraphiteArguments


def test_instantiation_accepts_valid_arguments():
    valid_dummy_a = 1
    valid_dummy_b = 1.2

    graphite_arguments = GraphiteArguments(
        valid_dummy_a,
        valid_dummy_b
    )

    assert(graphite_arguments.dummy_a == valid_dummy_a)
    assert(graphite_arguments.dummy_b == valid_dummy_b)


def test_instantiation_rejects_invalid_dummy_a():
    invalid_dummy_a = 2137
    valid_dummy_b = 1.2

    with pytest.raises(ValueError):
        GraphiteArguments(
            invalid_dummy_a,
            valid_dummy_b
        )


def test_instantiation_rejects_invalid_dummy_b():
    valid_dummy_a = 1
    invalid_dummy_b = 2.137

    with pytest.raises(ValueError):
        GraphiteArguments(
            valid_dummy_a,
            invalid_dummy_b
        )