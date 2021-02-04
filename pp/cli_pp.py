# -*- coding: utf-8 -*-
"""
Command line interface pp.
"""

import sys,os,subprocess,shutil
from types import SimpleNamespace
from pathlib import Path

import click

path_to_workspace = Path('/Users/etijskens/software/dev/workspace/')


def execute(cmds, logfun=None, stop_on_error=True, env=None, cwd=None):
    """Executes a list of OS commands, and logs with logfun.

    :param list cmds: list of OS commands (=list of list of str) or a single command (list of str)
    :parma callable logfun: a function to write output, typically
        ``logging.getLogger('et_micc').debug``.
    :returns int: return code of first failing command, or 0 if all
        commanbds succeed.
    """
    if isinstance(cmds[0], str):
        # this is a single command
        cmds = [cmds]

    for cmd in cmds:
        print(f"> {' '.join(cmd)}")
        try:
            # python >=3.7
            completed_process = subprocess.run(cmd, capture_output=True, env=env, cwd=cwd)
        except:
            # python <3.7, e.g 3.6.9:
            #   capture_output parameter does not exist.
            completed_process = subprocess.run(cmd, env=env, cwd=cwd,
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE,
                                               )
        if not logfun is None:
            if completed_process.returncode:
                logfun0 = logfun
                try:
                    logfun = logfun.__self__.warning
                except:
                    pass
                logfun(f"> {' '.join(cmd)}")
            if completed_process.stdout:
                logfun(' (stdout)\n' + completed_process.stdout.decode('utf-8'))
            if completed_process.stderr:
                logfun(' (stderr)\n' + completed_process.stderr.decode('utf-8'))
            if completed_process.returncode:
                logfun = logfun0
        if completed_process.returncode:
            if stop_on_error:
                return completed_process.returncode
    return 0


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


def _copy_micc_docs():
    print("Building micc html documentation")
    cmds =[['make','html']]
    execute(cmds,logfun=print,stop_on_error=False,cwd=str(path_to_workspace / 'et-micc/docs'))

    print("Copying micc html documentation")
    src = path_to_workspace / 'et-micc/docs/_build/html/'
    dst = path_to_workspace / 'pp/course-material/micc-documentation/'
    dst.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src,dst,dirs_exist_ok=True)

@main.command()
@click.pass_context
def copy_micc_docs(ctx):
    """Subcommand copy-micc-docs.
    
    """
    _copy_micc_docs()
    return 0

def _pptx():
    path_to_course_material =  path_to_workspace / 'pp/course-material'
    count = 0
    for root, dirs, files in os.walk(str(path_to_course_material)):
        proot = Path(root)
        for pptx in files:
            if pptx.endswith('.pptx') and not pptx.startswith('~$'):
                pdf = pptx.replace('.pptx','.pdf')
                path_to_pptx = proot / pptx
                path_to_pdf  = proot / pdf
                if path_to_pdf.stat().st_mtime < path_to_pptx.stat().st_mtime:
                    print(f"{path_to_pdf} not up to date!")
                    count += 1
    print(f"{count} .pptx files need to be updated.")
    return count

@main.command()
@click.pass_context
def pptx(ctx):
    """Check that all .pptx files are older than the corrsponding .pdf file"""
    return _pptx()

@main.command()
@click.pass_context
def check(ctx):
    count = 0
    _copy_micc_docs()
    count += _pptx()

    if count:
        print(f"Issues detected: {count}")

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
#eodf
