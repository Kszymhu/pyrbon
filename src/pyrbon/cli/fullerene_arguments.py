from dataclasses import dataclass

@dataclass
class FullereneArguments:
    '''
    Class for `Pyrbon fullerene` command line arguments.

    Attributes
    ----------
    dummy_a : int
        Dummy argument A. Cannot be 2137.
    dummy_b : float
        Dummy argument B. Cannot be 2.137.
    '''

    _dummy_a: int
    _dummy_b: float

    def __post_init__(self):
        if not isinstance(self._dummy_a, int):
            raise TypeError(f'Dummy argument A has to be of type `int`. Current: {type(self._dummy_a)}')
        if self._dummy_a == 2137:
            raise ValueError(f'Dummy argument A cannot be 2137. Current: {self._dummy_a}')

        if (not isinstance(self._dummy_b, float)) and (not isinstance(self._dummy_b, int)):
            raise TypeError(f'Dummy argument B has to be of type `float` or `int`. Current: {type(self._dummy_a)}')
        if self._dummy_b == 2.137:
            raise ValueError(f'Dummy argument B cannot be 2.137. Current: {self._dummy_b}')

    @property
    def dummy_a(self):
        '''
        Get the `dummy_a` field.

        Returns
        -------
        dummy_a : int
            Dummy argument A.
        '''
        return self._dummy_a


    @property
    def dummy_b(self):
        '''
        Get the `dummy_b` field.

        Returns
        -------
        dummy_b : int
            Dummy argument B.
        '''
        return self._dummy_b