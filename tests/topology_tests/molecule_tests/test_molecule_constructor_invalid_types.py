import numpy as np
import pytest

from pyrbon.topology.atom import Atom
from pyrbon.topology.molecule import Molecule

'''
Molecule constructor should reject invalid argument types.
'''


def test_constructor_rejects_atoms_heterogenous_list() -> None:
    atoms: list = [
        Atom(np.array([1, 2, 3]), 'H'),
        5,
        'Shrimp'
    ]

    description = 'Molecule'

    with pytest.raises(TypeError):
        Molecule(atoms, description)


def test_constructor_rejects_description_none() -> None:
    atoms: list[Atom] = [
        Atom(np.array([1, 2, 3]), 'H'),
        Atom(np.array([4, 5, 6]), 'H'),
        Atom(np.array([7, 8, 9]), 'H')
    ]

    description = None

    with pytest.raises(TypeError):
        Molecule(atoms, description)