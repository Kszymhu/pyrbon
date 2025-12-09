import numpy as np

from pyrbon.topology.atom import Atom

'''
Atom constructor should accept:
    - NumPy arrays of shapes (3,), (3, 1) or (1, 3) for `coordinates`
    - Any str for `element`, including empty ones
'''

def test_constructor_works_with_coordinates_shape_3() -> None:
    coordinates = np.zeros((3,))
    element = 'H'

    atom = Atom(coordinates, element)

    assert (atom.coordinates == coordinates.flatten()).all
    assert atom.element == element


def test_constructor_works_with_coordinates_shape_3_1() -> None:
    coordinates = np.zeros((3, 1))
    element = 'H'

    atom = Atom(coordinates, element)

    assert (atom.coordinates == coordinates.flatten()).all
    assert atom.element == element


def test_constructor_works_with_coordinates_shape_1_3() -> None:
    coordinates = np.zeros((1, 3))
    element = 'H'

    atom = Atom(coordinates, element)

    assert (atom.coordinates == coordinates.flatten()).all
    assert atom.element == element


def test_constructor_works_with_element_empty_str() -> None:
    coordinates = np.zeros((3))
    element = ''

    atom = Atom(coordinates, element)

    assert (atom.coordinates == coordinates.flatten()).all
    assert atom.element == element   