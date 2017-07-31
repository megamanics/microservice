"""
This is pure python implementation of search algorithm

Program's goal is to find the best two items.

    It takes two inputs:
    1. A filename with a list of sorted prices
    2. The balance of your gift card
    3. the no of gifts to consider. defaults to 2 [optional]

    If no two items have a sum that is less than or equal to the balance on the gift card,
    print “Not possible”. You don’t have to return every possible pair that is under the
    balance, just one such pair.


Problem Statement:
You have been given a gift card that is about to expire and you want to buy gifts for 2 friends.
You want to spend the whole gift card, or if that’s not an option as close to it as possible. You
have a list of sorted prices for a popular store that you know they both like to shop at. Your
challenge is to find two distinct items in the list whose sum is minimally under (or equal to) the
gift card balance.

"""
import itertools as it
import fire
import pandas as pd
import numpy as np

def findpair(pfile='prices.txt', balance=2500, giftno=2, debug=False):
    """ Find afforable gift combination while maximizing gift card utilization.
    Parameters
    ----------
    pfile : string, (default is 'prices.txt')
        The price file  should contain two columns:
        1. A unique identifier of the item. You can assume there are no duplicates.
        2. The value of that item in cents.
           It is always a positive integer that represents the price in cents (1000 = $10.00).
    balance : int, (defaults to = 2500)
        It is always a positive integer  that represents
        the balance of giftcard in cents
    giftno : int, (defaults=2)
        The no of gifts to consider.

    Returns
    -------
    Tuple
        A series of distinct items in the list
        whose sum is minimally under (or equal to) the gift card balance.

    Example of the prices file
    --------------------------
    cat prices.txt
    Candy Bar, 500
    Paperback Book, 700
    Detergent, 1000
    Headphones, 1400
    Earmuffs, 2000
    Bluetooth Stereo, 6000

    Usage:   find_pair.py -- --help to display usage
             find_pair.py [PFILE] [BALANCE] [GIFTNO]
             find_pair.py [--pfile PFILE] [--balance BALANCE] [--giftno GIFTNO]

    """
    prices = pd.read_csv(pfile, header=None, names=['item', 'price'])
    affordable = []
    minimal = ('Not possible',balance)
    for items in it.combinations(prices.index, giftno):
        total = np.sum([prices.price[b] for b in items])
        newbalance = balance - total
        if total <= balance and newbalance < minimal[1]:
            affordable = [(prices.item[idx], prices.price[idx])
                          for idx in items]
            minimal = (affordable,newbalance,total)
            if debug:
                print(minimal)
    return minimal

def test_findpair():
    """
        @TODO: add test functions
    """
    assert findpair('prices.txt', 2500, 5) == "Not possible"

if __name__ == "__main__":
    fire.Fire(findpair)
