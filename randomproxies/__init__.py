"""Random Proxies
This script allows the user to generate a random proxie from a list of proxies contained on UserAgent.csv
Methods:
--------
getProxie():    Returns a random proxie from the list
"""

import random
import os


def __getArray(f):
    headers = []
    for row in f:
        if len(row)>0:
            while row[len(row)-1] == ' ':
                row = row[0:len(row)-1]
            headers.append(row)

    return headers

def getProxie():
    """ A function that returns a random proxie from UserAgent.csv
    Parameters:
    -----------
    (No Parameters)
    returns:
    -------
    json: object with the proxie http and https
    """
    fpath= os.path.dirname(os.path.realpath(__file__)) + '/UserAgent.csv'
    f = open(fpath, "r").read().split('\n')
    headers = __getArray(f)

    proxie = random.choice(headers)

    return {
            "http": proxie,
            "https": proxie
        }   