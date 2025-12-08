import argparse

def create_parser() -> argparse.ArgumentParser:
    '''
    Create an argument parser.

    Returns
    -------
    argument_parser: argparse.ArgumentParser
        Argument parser.
    '''
    parser = argparse.ArgumentParser(
        prog='Pyrbon',
        description='Command-line tool for generating carbon allotrope structures.',
    )

    subparsers = parser.add_subparsers(
        required=True,
        help='Individual generators',
        dest='generator'
    )

    # Diamond generator
    diamond_parser = subparsers.add_parser(
        name='diamond',
        prog='Pyrbon diamond',
        description='Pytbon\'s diamond generator.'
    )

    diamond_parser.add_argument(
        '-a', '--dummy_a',
        type=int,
        required=True,
        help='Dummy argument A.'
    )
    diamond_parser.add_argument(
        '-b', '--dummy_b',
        type=float,
        required=True,
        help='Dummy argument B.'
    )

    # Fullerene generator
    fullerene_parser = subparsers.add_parser(
        name='fullerene',
        prog='Pyrbon fullerene',
        description='Pyrbon\'s fullerene generator.'
    )

    fullerene_parser.add_argument(
        '-a', '--dummy_a',
        type=int,
        required=True,
        help='Dummy argument A.'
    )
    fullerene_parser.add_argument(
        '-b', '--dummy_b',
        type=float,
        required=True,
        help='Dummy argument B.'
    )

    # Graphene generator
    graphene_parser = subparsers.add_parser(
        name='graphene',
        prog='Pyrbon graphene',
        description='Pyrbon\'s graphene generator.'
    )

    graphene_parser.add_argument(
        '-a', '--dummy_a',
        type=int,
        required=True,
        help='Dummy argument A.'
    )
    graphene_parser.add_argument(
        '-b', '--dummy_b',
        type=float,
        required=True,
        help='Dummy argument B.'
    )

    # Graphite generator
    graphite_parser = subparsers.add_parser(
        name='graphite',
        prog='Pyrbon graphite',
        description='Pyrbon\'s graphite generator.'
    )

    graphite_parser.add_argument(
        '-a', '--dummy_a',
        type=int,
        required=True,
        help='Dummy argument A.'
    )
    graphite_parser.add_argument(
        '-b', '--dummy_b',
        type=float,
        required=True,
        help='Dummy argument B.'
    )

    # MWCNT generator
    mwcnt_parser = subparsers.add_parser(
        name='mwcnt',
        prog='Pyrbon mwcnt',
        description='Pyrbon\'s multi-walled carbon nanotube generator.',
    )

    mwcnt_parser.add_argument(
        '-a', '--dummy_a',
        type=int,
        required=True,
        help='Dummy argument A.'
    )
    mwcnt_parser.add_argument(
        '-b', '--dummy_b',
        type=float,
        required=True,
        help='Dummy argument B.'
    )

    # PAH generator
    pah_parser = subparsers.add_parser(
        name='pah',
        prog='Pyrbon Ppah',
        description='Pyrbon\'s polycyclic aromatic hydrocarbon generator.',
    )
    pah_parser.add_argument(
        '-a', '--dummy_a',
        type=int,
        required=True,
        help='Dummy argument A.'
    )
    pah_parser.add_argument(
        '-b', '--dummy_b',
        type=float,
        required=True,
        help='Dummy argument B.'
    )

    # Parchment generator
    parchment_parser = subparsers.add_parser(
        name='parchment',
        prog='Pyrbon parchment',
        description='Pyrbon\'s parchment carbon nanotube generator.',
    )
    parchment_parser.add_argument(
        '-a', '--dummy_a',
        type=int,
        required=True,
        help='Dummy argument A.'
    )
    parchment_parser.add_argument(
        '-b', '--dummy_b',
        type=float,
        required=True,
        help='Dummy argument B.'
    )

    # SWCNT generator
    swcnt_parser = subparsers.add_parser(
        name='swcnt',
        prog='Pyrbon swcnt',
        description='Pyrbon\'s single-walled carbon nanotube generator.',
    )
    swcnt_parser.add_argument(
        '-a', '--dummy_a',
        type=int,
        required=True,
        help='Dummy argument A.'
    )
    swcnt_parser.add_argument(
        '-b', '--dummy_b',
        type=float,
        required=True,
        help='Dummy argument B.'
    )

    return parser