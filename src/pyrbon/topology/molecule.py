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
        '''
        Get the `atoms` field.

        Returns
        -------
        atoms: list[Atom]
            Atoms in this molecule.
        '''
        return self._atoms


    @property
    def description(self) -> list[Atom]:
        '''
        Get the `description` field.

        Returns
        -------
        description: str
            Description of this molecule.
        '''
        return self._description
    

    def add_atom(self, atom: Atom) -> None:
        '''
        Add an atom to this molecule.

        Parameters
        ----------
        atom: Atom
            Atom to add.
        '''

        if not isinstance(atom, Atom):
            raise TypeError(f'Cannot add a non-atom element to `atom`. Current: {type(atom)}')

        self._atoms.append(atom)
    

    def to_xyz_str(self, decimal_places: int = 5, sep: str = '') -> str:
        '''
        Generate a XYZ file str about the molecule.

        Parameters
        ----------
        decimal_places: int
            Decimal places to include in the atom lines (default: 5).
        sep: str
            Separator to put between sections of the atom lines (default: whitespace).

        Returns
        -------
        xyz_str: str
            XYZ file str about the atom.
        '''

        atom_lines: list[str] = []

        atom_lines.append(str(len(self.atoms)))
        atom_lines.append(self.description)

        for atom in self.atoms:
            atom_lines.append(atom.to_xyz_line(
                decimal_places, sep
            ))

        xyz_str = '\n'.join(atom_lines)

        return xyz_str