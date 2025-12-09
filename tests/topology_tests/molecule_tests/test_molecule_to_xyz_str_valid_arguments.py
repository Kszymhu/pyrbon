import numpy as np

from pyrbon.topology.atom import Atom
from pyrbon.topology.molecule import Molecule

'''
Molecule.to_xyz_str() should work with any allowed decimal places and separators.
'''

def test_to_xyz_str_works_with_single_atom() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')
    molecule = Molecule(atom, 'test')
    
    xyz_str = molecule.to_xyz_str(decimal_places=5, sep=' ')
    xyz_str_real = \
        '1\n' +\
        'test\n' +\
        'C 1.00000 2.00000 3.00000'
    assert xyz_str == xyz_str_real


def test_to_xyz_str_works_with_multiple_atoms() -> None:
    atoms = [
        Atom(np.array([1, 2, 3]), 'C'),
        Atom(np.array([2, 3, 4]), 'C'),
        Atom(np.array([3, 4, 5]), 'C'),
        Atom(np.array([4, 5, 6]), 'C'),
        Atom(np.array([5, 6, 7]), 'C'),
        Atom(np.array([6, 7, 8]), 'C'),
        Atom(np.array([7, 8, 9]), 'C'),
        Atom(np.array([6, 7, 8]), 'C'),
        Atom(np.array([5, 6, 7]), 'C'),
        Atom(np.array([4, 5, 6]), 'C')
    ]

    molecule = Molecule(atoms, 'test')

    xyz_str = molecule.to_xyz_str(decimal_places=3, sep=' ')
    xyz_str_real = \
        '10\n' +\
        'test\n' +\
        'C 1.000 2.000 3.000\n' +\
        'C 2.000 3.000 4.000\n' +\
        'C 3.000 4.000 5.000\n' +\
        'C 4.000 5.000 6.000\n' +\
        'C 5.000 6.000 7.000\n' +\
        'C 6.000 7.000 8.000\n' +\
        'C 7.000 8.000 9.000\n' +\
        'C 6.000 7.000 8.000\n' +\
        'C 5.000 6.000 7.000\n' +\
        'C 4.000 5.000 6.000'

    assert xyz_str == xyz_str_real