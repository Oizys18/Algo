# SWEA 4865
"""
str1 
str2
"""

# str1 = "XYPV"
# str2 = "EOGGXYPVSY"
# dct = {}
# for i in str1:
#     dct[i] = 0 

import sys
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    dct = {}
    str1 = ''
    str2 = ''
    str1,str2 = input(), input()
    for i in str1:
        dct[i] = 0 
    for j in str2:
        if j in dct.keys():
            dct[j] += 1
    cnt = 0
    for k,v in dct.items():
        if v > cnt : 
            cnt = v
    print("#{0} {1}".format(T+1,cnt))
        
