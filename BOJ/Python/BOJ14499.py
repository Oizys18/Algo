import sys 
sys.stdin = open('BOJ14499.txt','r')
from pprint import pprint as pp 

N,M,x,y,k = map(int,input().split())
mat = [[*map(int,input().split())] for _ in range(N)]
orders = [*map(int,input().split())]
dr = [0,(0,1),(0,-1),(-1,0),(1,0)]

def isMap(x,y):
    return 0 <= x < N and 0 <= y < M 

def move(order,x,y):
    pass 


print(N,M,x,y,k)
pp(mat)
print(orders)