import numpy as np
import pytest

from pyrbon.topology.atom import Atom

'''
Atom.to_xyz_line() should reject non-int decimal_places and non-str sep.
'''

def test_to_xyz_line_rejects_decimal_places_float() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')
    decimal_places = 2.0

    with pytest.raises(TypeError):
        xyz_line = atom.to_xyz_line(decimal_places=decimal_places)


def test_to_xyz_line_rejects_decimal_places_None() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')
    decimal_places = None

    with pytest.raises(TypeError):
        xyz_line = atom.to_xyz_line(decimal_places=decimal_places)


def test_to_xyz_line_rejects_sep_int() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')
    sep = 2

    with pytest.raises(TypeError):
        xyz_line = atom.to_xyz_line(sep=sep)


def test_to_xyz_line_rejects_sep_None() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')
    sep = None

    with pytest.raises(TypeError):
        xyz_line = atom.to_xyz_line(sep=sep)