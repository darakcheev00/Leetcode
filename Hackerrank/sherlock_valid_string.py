#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    counts = {}
    
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
        
    countsOfCounts = {}
    for c, val in counts.items():
        if val in countsOfCounts:
            countsOfCounts[val] += 1
        else:
            countsOfCounts[val] = 1
            
        if len(countsOfCounts) > 2:
            return "NO"
    
    if len(countsOfCounts) == 1:
        return "YES"

    items = [(key,val) for key,val in countsOfCounts.items()]
    
    if items[0][1] != 1 and items[1][1] != 1:
        return "NO"
        
    less = items[0] if items[0][1] == 1 else items[1]
    more = items[1] if items[0][1] == 1 else items[0]
    
    if less[0] == 1 or less[0] - more[0] == 1:
        return "YES"
    
    return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
