import pytest

from pyrbon.cli.graphene_arguments import GrapheneArguments


def test_instantiation_accepts_valid_arguments():
    valid_dummy_a = 1
    valid_dummy_b = 1.2

    graphene_arguments = GrapheneArguments(
        valid_dummy_a,
        valid_dummy_b
    )

    assert(graphene_arguments.dummy_a == valid_dummy_a)
    assert(graphene_arguments.dummy_b == valid_dummy_b)


def test_instantiation_rejects_invalid_dummy_a():
    invalid_dummy_a = 2137
    valid_dummy_b = 1.2

    with pytest.raises(ValueError):
        GrapheneArguments(
            invalid_dummy_a,
            valid_dummy_b
        )


def test_instantiation_rejects_invalid_dummy_b():
    valid_dummy_a = 1
    invalid_dummy_b = 2.137

    with pytest.raises(ValueError):
        GrapheneArguments(
            valid_dummy_a,
            invalid_dummy_b
        )