import sys
sys.stdin=open('BOJ2310.txt','r')


from collections import defaultdict
while True:
    N = int(input())
    if N == 0:
        break
    Map = defaultdict()
    data = [input().split() for _ in range(N)]
    for d in data:
        race, cost, *paths = d
        print(race,cost,paths)


