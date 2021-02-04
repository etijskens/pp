# -*- coding: utf-8 -*-
"""
Command line interface pp.
"""

import sys
from types import SimpleNamespace
import shutil
from pathlib import Path

import click


@click.group()
@click.option('-v', '--verbosity', count=True
             , help="The verbosity of the program output."
             , default=1
             )
@click.pass_context
def main(ctx, verbosity):
    """Command line interface pp.
    
    A 'hello' world CLI example.
    """
    # store global options in ctx.obj
    ctx.obj = SimpleNamespace(verbosity=verbosity)

    click.echo(f"running pp")


@main.command()
@click.pass_context
def copy_micc_docs(ctx):
    """Subcommand copy-micc-docs.
    
    """
    path_to_workspace = Path('/Users/etijskens/software/dev/workspace/')
    src = path_to_workspace / 'et-micc/docs/_build/html/'
    dst = path_to_workspace / 'pp/course-material/micc-documentation/'
    dst.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src,dst,dirs_exist_ok=True)

    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
#eodf
