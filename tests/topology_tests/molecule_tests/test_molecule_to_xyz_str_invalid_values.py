import numpy as np
import pytest

from pyrbon.topology.atom import Atom
from pyrbon.topology.molecule import Molecule

'''
Molecule.to_xyz_str() should reject negative decimal_places
by letting Atom.to_xyz_line() throw ValueErrors.
'''

def test_to_xyz_str_rejects_decimal_places_negative() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')
    molecule = Molecule(atom, 'test')

    decimal_places = -1

    with pytest.raises(ValueError):
        molecule.to_xyz_str(decimal_places=decimal_places)