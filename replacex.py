"""
Write a program that will print out every possible combination
where you replace X in a given string with ​both 0 and 1.
"""

import math
import fire
import numpy as np

def replace(xstring='X1X0X'):
    """ Replace X with every possible combination where you replace the X with ​both 0 and 1.

    Parameters
    ----------
    xstring : string, (default is 'X1X0X')
    string composed of only 1s, 0s, and Xs.

    Returns
    -------
    Prints a list of possible combinations while replacing X with 1 and 0.

    Example
    -------
    $ replacex.py X0
    00
    10
    $ replacex.py 10X10X0
    1001000
    1001010
    1011000
    1011010

    replacex.py -- --help to display usage
    """
    xnp = np.array([x for x in xstring])
    xpos = np.where(xnp == 'X')[0]
    nofx = len(xpos)
    bigo = math.pow(2, nofx) #Big O Notation for this program
    packst = '{:0>' + str(nofx) + '}' #pad zeros
    for num in range(int(bigo)):
        binarynum = packst.format(bin(num).split('b')[1]) #split binary number in chars
        xnp.flat[xpos] = [binum for binum in binarynum] #assign 1/0 in place of X
        comp = [print(x, end='') for x in xnp] #print one combination
        print() #print newline
    return "done"

def test_replacex():
    """
        @TODO: add more test cases
    """
    assert replace('10X10X0') == "done"


if __name__ == "__main__":
    #@TODO: Add validations for inputs
    fire.Fire(replace)
