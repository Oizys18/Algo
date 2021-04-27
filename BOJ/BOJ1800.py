# BOJ1800 인터넷 설치 
import sys
sys.stdin = open('BOJ1800.txt','r')
from pprint import pprint as pp
from time import time
from collections import deque,defaultdict

start = time()

N,P,K = map(int,input().split())
edges = defaultdict(list)
for i in range(N):
    edges[i] = []

mat = [list(map(int,input().split())) for _ in range(P)]

for p in range(P):
    A,B,price = mat[p]
    edges[A].append((A,B,price))
    edges[B].append((B,A,price))


def prim(start,edges):



print(time()-start)