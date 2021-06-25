import sys
sys.stdin = open('BOJ1020.txt','r')
from pprint import pprint as pp

time = [int(i) for i in input()]
N = len(time)
cnt = {
    1:2,
    2:5,
    3:5,
    4:4,
    5:5,
    6:6,
    7:3,
    8:7,
    9:5,
    0:6
}

def count(time):
    total = 0
    for t in time:
        total += cnt[t]
    return total

def solve(time):
    if count(time) == N:
        return time
    else:
        solve(time+1)


