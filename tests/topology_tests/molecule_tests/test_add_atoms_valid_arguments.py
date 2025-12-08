import numpy as np

from pyrbon.topology.atom import Atom
from pyrbon.topology.molecule import Molecule

'''
Molecule.add_atoms() should accept:
    - Only a single argument of type Atom
'''

def test_add_atoms_accepts_atom():
    atom_a = Atom(np.array([0, 1, 2]), 'C')
    atom_b = Atom(np.array([3, 4, 5]), 'C')

    molecule = Molecule(atom_a, 'test')
    molecule.add_atom(atom_b)

    assert atom_a in molecule.atoms
    assert atom_b in molecule.atoms


def test_add_atoms_accepts_atom_when_molecule_created_with_no_atoms():
    atom = Atom(np.array([0, 1, 2]), 'C')

    molecule = Molecule(None, 'test')
    molecule.add_atom(atom)

    assert atom in molecule.atoms