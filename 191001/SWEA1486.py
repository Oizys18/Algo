#SWEA1486

import sys
sys.stdin = open('input2.txt','r')
import itertools

for T in range(int(input())):
    N, B = map(int,input().split())
    people = list(map(int,input().split()))
    bigger = []
    temp = 0

    for j in range(N,-1,-1):
        for i in itertools.combinations(people,j):
            if temp != 0 and sum(i) > temp:
                continue
            if sum(i) >= B:
                temp = sum(i)
    print("#{} {}".format(T+1,temp-B))
