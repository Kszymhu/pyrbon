import numpy as np

from pyrbon.topology.atom import Atom
from pyrbon.topology.molecule import Molecule

'''
Molecule constructor should accept:
    - A list[Atom], a single Atom, or None for atoms
    - Any str for description
'''

def test_constructor_accepts_atoms_list() -> None:
    atoms: list[Atom] = [
        Atom(np.array([1, 2, 3]), 'H'),
        Atom(np.array([4, 5, 6]), 'H'),
        Atom(np.array([7, 8, 9]), 'H')
    ]

    description = 'Molecule'

    molecule = Molecule(atoms, description)

    assert(molecule.atoms == atoms)
    assert(molecule.description == description)


def test_constructor_accepts_single_atom() -> None:
    atoms = Atom(np.array([1, 2, 3]), 'H')

    description = 'Molecule'

    molecule = Molecule(atoms, description)

    assert(molecule.atoms == [atoms])
    assert(molecule.description == description)


def test_constructor_accepts_none() -> None:
    atoms = None

    description = 'Molecule'

    molecule = Molecule(atoms, description)

    assert(molecule.atoms == [])
    assert(molecule.description == description)


def test_constructor_accepts_description_empty_str() -> None:
    atoms: list[Atom] = [
        Atom(np.array([1, 2, 3]), 'H'),
        Atom(np.array([4, 5, 6]), 'H'),
        Atom(np.array([7, 8, 9]), 'H')
    ]

    description = ''

    molecule = Molecule(atoms, description)

    assert(molecule.atoms == atoms)
    assert(molecule.description == description)