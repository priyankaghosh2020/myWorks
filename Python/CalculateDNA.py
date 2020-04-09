#!/bin/python3

import math
import os
import random
import re
import sys


def calculateDNA (genes , health , first , last , d) :
    sum = 0
    for indx in range(len(d)) :
        st = d[indx:]
        for i , g in enumerate(genes) :
            if i >= first and i <= last :
                try :
                    if st and st.index(g) == 0 :
                        sum += health[i]
                except :
                    pass
    return sum

if __name__ == '__main__':
    n = 6

    genes = 'a b c aa d b'.rstrip().split()

    health = list(map(int, '1 2 3 4 5 6'.rstrip().split()))

    s = 3
    max = min = 0

    # for s_itr in range(s):
    firstLastd = '0 4 xyz'.split()

    first = int(firstLastd[0])

    last = int(firstLastd[1])

    d = firstLastd[2]

    sum = calculateDNA (genes , health , first , last , d)
    if max < sum :
        max = sum

    if min == 0 or min > sum :
        min = sum

    print (str(min) + ' ' + str(max))





