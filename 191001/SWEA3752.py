import sys
sys.stdin = open('input3.txt','r')
import itertools
from pprint import pprint as pp 


def solve(k, s):
    if visited[k][s]: return
    visited[k][s] = 1
    if k == N:
        return
    else:
        # print(s)
        solve(k + 1, s)
        # print(s + scores[k])
        solve(k + 1, s + scores[k])
        
for tc in range(1, int(input()) + 1):
    N = int(input())
    scores = list(map(int, input().split()))

    visited = [[0] * (sum(scores) + 1) for _ in range(N + 1)]
    solve(0, 0)
    pp(visited)
    print('#%d'%tc, sum(visited[N]))


"""
#1 4680
#2 4566
#3 5646
#4 4891
#5 4357
#6 4773
#7 5482
#8 4971
#9 5158
#10 4847
"""






















