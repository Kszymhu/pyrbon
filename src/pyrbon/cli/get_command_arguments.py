import argparse
from typing import Union

from pyrbon.cli.diamond_arguments import DiamondArguments
from pyrbon.cli.fullerene_arguments import FullereneArguments
from pyrbon.cli.graphene_arguments import GrapheneArguments
from pyrbon.cli.graphite_arguments import GraphiteArguments
from pyrbon.cli.mwcnt_arguments import MwcntArguments
from pyrbon.cli.parchment_arguments import ParchmentArguments
from pyrbon.cli.swcnt_arguments import SwcntArguments

type CommandArguments = Union[
    DiamondArguments,
    FullereneArguments,
    GrapheneArguments,
    GraphiteArguments,
    MwcntArguments,
    ParchmentArguments,
    SwcntArguments
]

def get_command_arguments(arguments: argparse.Namespace) -> CommandArguments:
    '''
    Convert parsed arguments into one of the command-specific argument classes.

    Parameters
    ----------
    arguments: argparse.Namespace
        Parsed arguments.
    
    Returns
    -------
    command_arguments: CommandArguments
        Command-specific arguments.
    '''

    if arguments.generator == 'diamond':
        return DiamondArguments(
            arguments.dummy_a,
            arguments.dummy_b
        )
    elif arguments.generator == 'fullerene':
        return FullereneArguments(
            arguments.dummy_a,
            arguments.dummy_b
        )
    elif arguments.generator == 'graphene':
        return GrapheneArguments(
            arguments.dummy_a,
            arguments.dummy_b
        )
    elif arguments.generator == 'graphite':
        return GraphiteArguments(
            arguments.dummy_a,
            arguments.dummy_b
        )
    elif arguments.generator == 'mwcnt':
        return MwcntArguments(
            arguments.dummy_a,
            arguments.dummy_b
        )
    elif arguments.generator == 'parchment':
        return ParchmentArguments(
            arguments.dummy_a,
            arguments.dummy_b
        )
    elif arguments.generator == 'swcnt':
        return SwcntArguments(
            arguments.dummy_a,
            arguments.dummy_b
        )