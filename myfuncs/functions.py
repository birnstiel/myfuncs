# this is to access data of the package
from pkg_resources import resource_filename
import os
import numpy as np

f = 2


def mypower(a):
    """
    this is a stupid function that takes a to the f's power.

    Argument
    --------

    a : scalar
        number to be taken to the power of f
    """
    return a**f


def get_data(i):
    fname = resource_filename(__name__, os.path.join(f'data{i}', 'data.txt'))
    if os.path.isfile(fname):
        return np.loadtxt(fname, delimiter=',')
    else:
        raise FileExistsError('No such data file exists in the package!')
