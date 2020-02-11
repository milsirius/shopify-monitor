"""Random Headers
This script allows the user to generate a random header from a list of proxies contained on UserAgent.csv
Methods:
--------
getProxie():    Returns a random header from the list
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

def getHeader():
    """ A function that returns a random header from UserAgent.csv
    Parameters:
    -----------
    (No Parameters)
    returns:
    -------
    json: object with the header
    """
    fpath= os.path.dirname(os.path.realpath(__file__)) + '/UserAgent.csv'
    f = open(fpath, "r").read().split('\n')
    headers = __getArray(f)

    return {'User-Agent': random.choice(headers)}    