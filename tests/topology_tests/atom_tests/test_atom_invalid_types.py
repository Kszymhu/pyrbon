import numpy as np
import pytest

from pyrbon.topology.atom import Atom

'''
Atom constructor should reject invalid argument types.
'''

def test_constructor_rejects_coordinates_list():
    coordinates = [0.0, 0.0, 0.0]
    element = 'H'

    with pytest.raises(TypeError):
        Atom(coordinates, element)


def test_constructor_rejects_coordinates_tuple():
    coordinates = (0.0, 0.0, 0.0)
    element = 'H'

    with pytest.raises(TypeError):
        Atom(coordinates, element)


def test_element_rejects_integer():
    coordinates = np.zeros((3,))
    element = 1

    with pytest.raises(TypeError):
        Atom(coordinates, element)
