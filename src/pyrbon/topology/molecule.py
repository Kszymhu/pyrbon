from pyrbon.topology.atom import Atom


class Molecule:
    '''
    Class representing a molecule.

    Attributes
    ----------
    atoms: list[Atom]
        Atoms in this molecule.
    description: str
        Description of this molecule.
    '''

    _atoms: list[Atom]
    _description: str


    def __init__(
            self,
            atoms: list[Atom] | None,
            description: str
    ) -> None:
        '''
        Parameters
        ----------
        atoms: list[Atom] | Atom | None
            Atoms in this molecule. Can be a list of Atoms, a single Atom, or None.
        description: str
            Description of this molecule.
        '''
        if atoms is None:
            self._atoms = []
        elif isinstance(atoms, Atom):
            self._atoms = [atoms]
        elif isinstance(atoms, list) and (len(atoms) == 0 or all(isinstance(x, Atom) for x in atoms)):
            self._atoms = atoms
        else:
            raise TypeError(f'Atoms need to be either a list of Atoms, a single Atom, or None. Current: {type(atoms)}')

        if isinstance(description, str):
            self._description = description
        else:
            raise TypeError(f'Description has to be a str. Current: {type(description)}')
        

    @property
    def atoms(self) -> list[Atom]:
        return self._atoms


    @property
    def description(self) -> list[Atom]:
        return self._description