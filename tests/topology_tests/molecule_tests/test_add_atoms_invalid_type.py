import numpy as np
import pytest

from pyrbon.topology.atom import Atom
from pyrbon.topology.molecule import Molecule

'''
Molecule.add_atoms() should reject:
    - Anything that's not an Atom
'''

def test_add_atoms_rejects_int() -> None:
    atom_a = Atom(np.array([0, 1, 2]), 'C')
    atom_b = 2137

    molecule = Molecule(atom_a, 'test')

    with pytest.raises(TypeError):
        molecule.add_atom(atom_b)


def test_add_atoms_rejects_list_of_atoms() -> None:
    atom_a = Atom(np.array([0, 1, 2]), 'C')
    atom_b = [Atom(np.array([3, 4, 5]), 'C')]

    molecule = Molecule(atom_a, 'test')

    with pytest.raises(TypeError):
        molecule.add_atom(atom_b)