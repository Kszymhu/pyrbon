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
