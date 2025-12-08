import numpy as np

from pyrbon.topology.atom import Atom

'''
Atom.to_xyz_line() should work with any allowed decimal places and separators.
'''

def test_to_xyz_line_accepts_regular() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')
    
    xyz_line = atom.to_xyz_line(decimal_places=5, sep=' ')

    assert xyz_line == 'C 1.00000 2.00000 3.00000'


def test_to_xyz_line_accepts_ungodly() -> None:
    atom = Atom(np.array([1, 2, 3]), 'C')

    xyz_line = atom.to_xyz_line(decimal_places=20, sep='shrimp')

    assert xyz_line == 'Cshrimp1.00000000000000000000shrimp2.00000000000000000000shrimp3.00000000000000000000'