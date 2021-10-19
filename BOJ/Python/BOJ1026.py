import sys 
sys.stdin = open('BOJ1026.txt','r')
from pprint import pprint as pp 

N = int(input())
A = [*map(int,input().split())]
B = [*map(int,input().split())]
A.sort()
B.sort()
answer = 0
for i in range(N):
    a = A.pop(0)
    b = B.pop()
    answer += a*b
print(answer) 
