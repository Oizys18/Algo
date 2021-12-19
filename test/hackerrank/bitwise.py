#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bitwiseEquations' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER_ARRAY b
#

def bitwiseEquations(a: [int], b: [int]) -> [int]:
    N = len(a)
    answer = []

    def getValue(adds: int, xors: int) -> int:
        # adds = 4 xors = 2
        # A = 1
        A = (adds-xors)//2
        a = 0
        b = 0
        for i in range(40):
            Xi = (xors & (1 << i))  # 2 & 10  == 10
            Ai = (A & (1 << i))    # 1 & 10 == 0
            if a+b == adds and a ^ b == xors:
                break
            if (Xi == 0 and Ai == 0):
                pass
            elif (Xi == 0 and Ai > 0):
                a = ((1 << i) | a)  # 1
                b = ((1 << i) | b)  # 1

            elif (Xi > 0 and Ai == 0):
                b = ((1 << i) | b)  # 11
            else:
                return 0

        return 2*a + 3*b

    for i in range(N):
        answer.append(getValue(a[i], b[i]))

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = int(input().strip())
        b.append(b_item)

    result = bitwiseEquations(a, b)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
