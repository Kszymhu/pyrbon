import numpy as np
import pytest

from pyrbon.topology.atom import Atom
from pyrbon.topology.molecule import Molecule

'''
Molecule.to_xyz_str() should reject non-int decimal_places and non-str sep
by letting Atom.to_xyz_line() throw TypeErrors.
'''

def test_to_xyz_str_rejects_decimal_places_float() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')
    molecule = Molecule(atom, 'test')

    decimal_places = 2.0

    with pytest.raises(TypeError):
        molecule.to_xyz_str(decimal_places=decimal_places)


def test_to_xyz_str_rejects_decimal_places_None() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')
    molecule = Molecule(atom, 'test')

    decimal_places = None

    with pytest.raises(TypeError):
        molecule.to_xyz_str(decimal_places=decimal_places)


def test_to_xyz_str_rejects_sep_int() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')
    molecule = Molecule(atom, 'test')

    sep = 2

    with pytest.raises(TypeError):
        molecule.to_xyz_str(sep=sep)


def test_to_xyz_str_rejects_sep_None() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')
    molecule = Molecule(atom, 'test')

    sep = None

    with pytest.raises(TypeError):
        molecule.to_xyz_str(sep=sep)