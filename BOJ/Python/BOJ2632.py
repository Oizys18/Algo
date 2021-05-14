import sys
sys.stdin = open('BOJ2632.txt','r')
from pprint import pprint as pp 

N = int(input())
m,n = map(int,input().split())
A = [int(input()) for _ in range(m)]
B = [int(input()) for _ in range(n)]
print(m,n)
print(A)
print(B)