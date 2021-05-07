import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ1620.txt', 'r')

N,M = map(int,input().split())
pokeDex = [input() for _ in range(N)]
pokeDict = {pokeDex[i]:i for i in range(N)}
pp(pokeDex)
pp(pokeDict)

for _ in range(M):
    q = input()
    if q.isnumeric():
        print(pokeDex[int(q)-1])
    else:
        print(pokeDict[q]+1)