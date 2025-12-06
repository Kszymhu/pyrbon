import numpy as np
import pytest

from pyrbon.topology.atom import Atom

'''
Atom constructor should reject:
    - Arrays with different shapes than (3,), (3, 1) or (1, 3) for coordinates
'''

def test_constructor_rejects_coordinates_shape_4():
    coordinates = np.zeros((4,))
    element = 'H'

    with pytest.raises(ValueError):
        Atom(coordinates, element)


def test_constructor_rejects_coordinates_shape_4_1():
    coordinates = np.zeros((4, 1))
    element = 'H'

    with pytest.raises(ValueError):
        Atom(coordinates, element)


def test_constructor_rejects_coordinates_shape_1_4():
    coordinates = np.zeros((1, 4))
    element = 'H'

    with pytest.raises(ValueError):
        Atom(coordinates, element)


def test_constructor_rejects_coordinates_shape_3_3():
    coordinates = np.zeros((3, 3))
    element = 'H'

    with pytest.raises(ValueError):
        Atom(coordinates, element)


def test_constructor_rejects_coordinates_shape_1_1_1_3():
    coordinates = np.zeros((1, 1, 1, 3))
    element = 'H'

    with pytest.raises(ValueError):
        Atom(coordinates, element)