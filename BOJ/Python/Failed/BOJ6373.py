# https://www.acmicpc.net/problem/6373
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ6373.txt', 'r')
from itertools import cycle 
while True:
    try: 
        N = input()
        # NC = cycle(N)
        Nlen = len(N)
        totalCnt = 0
        start = N[0]
        print(start)
        for i in range(2,Nlen+1):
            print('i:',i)
            newN = str(int(N)*i)
            print('newN:',newN)
            print(newN.index(start))
            
    except:
        break