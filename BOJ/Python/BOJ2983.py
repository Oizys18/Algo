from pprint import pprint as pp
import sys
sys.stdin = open('BOJ2983.txt', 'r')

N, K = map(int, sys.stdin.readline().split())
jumps = sys.stdin.readline().strip()
plants = [tuple(map(int, sys.stdin.readline().split()))
          for _ in range(N)]
frog = plants.pop(0)

dr = {
    'A': lambda x: (x[0]+1, x[1]+1),
    'B': lambda x: (x[0]+1, x[1]-1),
    'C': lambda x: (x[0]-1, x[1]+1),
    'D': lambda x: (x[0]-1, x[1]-1),
}

while frog not in plants:
    frog = dr['A'](frog)
