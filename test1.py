"""
This is a basic python file which needs to pass pylint before
a commit.
"""
import os

import numpy


def afunc(x):
    """
    A dummy function to make sure pylint is activating.
    """
    print(os.getcwd())
    print(numpy.__version__)
    print(x)


afunc(5)
