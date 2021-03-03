#!/bin/bash

# Setting up the environment for micc
# Although this is a bash script, i have never run it. I simply copied al the
# commands into it, just for reminding myself and to avoid I run into the same
# problems over and over again.

#-------------------------------------------------------------------------------
# Install gh (github cli) with brew
#-------------------------------------------------------------------------------
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)' >> /home/user/.profile
eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
brew install gh

#-------------------------------------------------------------------------------
# Install git
#-------------------------------------------------------------------------------
sudo apt-get update
sudo apt-get install git

#-------------------------------------------------------------------------------
# Install pyenv
#-------------------------------------------------------------------------------
# install system libraries for pyenv
# this command has changed since last year, the page on realpython.com on pyenv is not up to date
sudo apt-get update; sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

sudo apt install curl

curl https://pyenv.run | bash

#-------------------------------------------------------------------------------
# install python with pyenv
#-------------------------------------------------------------------------------
pyenv install 3.9.1
pyenv global 3.9.1
# upgrade its pip
python -m pip install --upgrade pip

#-------------------------------------------------------------------------------
# install poetry
#-------------------------------------------------------------------------------
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
# to have poetry on the path, close the shell and reopen it, or execute
source $HOME/.poetry/env
# configure poetry to create venvs in the project directory
poetry config virtualenvs.in-project true

#-------------------------------------------------------------------------------
# Install pipx
#-------------------------------------------------------------------------------
python -m pip install --user pipx
python -m pipx ensurepath

#-------------------------------------------------------------------------------
# Install micc with pipx:
#-------------------------------------------------------------------------------
# You will need to open a new terminal or re-login for the PATH changes to take effect.
pipx install et-micc

#-------------------------------------------------------------------------------
# Install cmake:
#-------------------------------------------------------------------------------
sudo apt-get install cmake

#-------------------------------------------------------------------------------
# Install gfortran:
#-------------------------------------------------------------------------------
sudo apt-get install gfortran

#-------------------------------------------------------------------------------
# Install openmpi:
# needed for pip install mpi4py
#-------------------------------------------------------------------------------
sudo apt install openmpi-bin libopenmpi-dev

#-------------------------------------------------------------------------------
# Install pycharm CE:
#-------------------------------------------------------------------------------
# (using ubuntu software)
# open pycharm and install plugins (settings/plugins) for
# - CMake
# - Fortran language support
