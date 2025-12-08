import numpy as np
import pytest

from pyrbon.topology.atom import Atom

'''
Atom.to_xyz_line() should reject negative decimal_places.
'''

def test_to_xyz_line_rejects_decimal_places_negative() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')
    decimal_places = -1

    with pytest.raises(ValueError):
        xyz_line = atom.to_xyz_line(decimal_places=decimal_places)