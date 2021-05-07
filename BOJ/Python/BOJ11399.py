# ATM
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ11399.txt', 'r')

N = int(input())
times = [*map(int,input().split())]
times.sort()
total = 0
for i in range(N):
    total += times[i]*(N-i)
print(total)
