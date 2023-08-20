#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p = 0
    n = 0
    z = 0
    
    for a in arr:
        if a == 0:
            z += 1
        elif a > 0:
            p += 1
        else:
            n += 1
            
    print(p/len(arr))
    print(n/len(arr))
    print(z/len(arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
