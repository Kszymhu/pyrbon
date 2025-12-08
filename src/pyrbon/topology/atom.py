import numpy as np


class Atom:
    '''
    Class representing an atom.

    Attributes
    ----------
    coordinates: numpy.ndarray
        Cartesian coordinates of the atom.
    element: str
        Element of the atom.
    '''

    _coordinates: np.ndarray
    _element: str


    def __init__(
            self,
            coordinates: np.ndarray,
            element: str
    ) -> None:
        '''
        Parameters
        ----------
        coordinates: numpy.ndarray
            Cartesian coordinates of the atom.
        element: str
            Element of the atom.
        '''
        if not isinstance(coordinates, np.ndarray):
            raise TypeError(f'Coordinates have to be a NumPy array. Current: {type(coordinates)}')
        if coordinates.shape != (3,) and coordinates.shape != (3, 1) and coordinates.shape != (1, 3):
            raise ValueError(f'Coordinates have to be a NumPy array of shape either (3,), (3, 1) or (1, 3). Current: {coordinates.shape}')
        self._coordinates = coordinates.flatten()

        if not isinstance(element, str):
            raise TypeError(f'Element has to be an str. Current: {type(element)}')
        self._element = element


    @property
    def coordinates(self) -> np.ndarray:
        '''
        Get the `coordinates` field.

        Returns
        -------
        coordinates: np.ndarray
            Cartesian coordinates of the atom.
        '''
        return self._coordinates
    

    @property
    def element(self) -> str:
        '''
        Get the `element` field.

        Returns
        -------
        element: str
            Element of the atom.
        '''
        return self._element
    

    def to_xyz_line(self, decimal_places: int = 5, sep: str = '') -> str:
        '''
        Generate a XYZ file line about the atom.

        Parameters
        ----------
        decimal_places: int
            Decimal places to include in the line (default: 5).
        sep: str
            Separator to put between sections of the line (default: whitespace).

        Returns
        -------
        xyz_line: str
            XYZ file line about the atom.
        '''

        if not isinstance(decimal_places, int):
            raise TypeError(f'The number of decimal places has to be an int. Current: {type(decimal_places)}')
        
        if decimal_places < 0:
            raise ValueError(f'The number of decimal places has to be at least 0. Current: {decimal_places}')
        
        if not isinstance(sep, str):
            raise TypeError(f'The separator has to be a str. Current: {type(sep)}')

        x_str = f'{self.coordinates[0]:.{decimal_places}f}'
        y_str = f'{self.coordinates[1]:.{decimal_places}f}'
        z_str = f'{self.coordinates[2]:.{decimal_places}f}'

        return sep.join([self.element, x_str, y_str, z_str])
