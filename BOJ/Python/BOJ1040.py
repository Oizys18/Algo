import sys 
sys.stdin = open('BOJ1040.txt','r')
from pprint import pprint as pp 


N,K = input().split()
K = int(K)
print(N,K)

pointer = 0
temp = ''
for i,v in enumerate(N):
    if K:
        K-=1 
        
    print(i,v)