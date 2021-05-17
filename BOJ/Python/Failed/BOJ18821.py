import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ18821.txt', 'r')


T = int(input())
for _ in range(T):
    n = int(input())
    if n==1:
        print('E')
    else:
        print('O')