import sys
sys.stdin = open('BOJ16235.txt','r')
from pprint import pprint as pp


N,M,K = map(int,input().split())
land = [[5]*N for _ in range(N)]
nutrition = [[*map(int,input().split())] for _ in range(N)]
tree_info = [[*map(int,input().split())] for _ in range(M)]

def solve():
    pass

pp(land)
pp(nutrition)
pp(tree_info)