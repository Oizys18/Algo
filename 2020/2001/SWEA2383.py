# 점심식사
import itertools
from pprint import pprint as pp
import sys
sys.stdin = open('2383.txt', 'r')


def checkTime(stair_queue, stair_length, x, y):
    timeLi = []
    for a, b in stair_queue:
        timeLi.append(abs(a-x) + abs(b-y))
    timeLi.sort()
    
    time = 1
    stair_q = []
    while True:
        for p in range(timeLi):
            if timeLi[p] >= stair_length and len(stair_q) <= 3:
                stair_q.append(timeLi[p])
                timeLi[p] = 0



T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    mat = [[*map(int, input().split())] for _ in range(N)]
    people = set()
    stair1 = 0
    stair2 = 0
    for x in range(N):
        for y in range(N):
            if mat[x][y] == 1:
                people.add((x, y))
            elif mat[x][y] > 1:
                if not stair1:
                    stair1 = [(x, y), mat[x][y]]
                else:
                    stair2 = [(x, y), mat[x][y]]

    res = 100000
    for population in range(len(people)+1):
        for choice in itertools.combinations(people, population):
            stair1_queue = set([*choice])
            stair2_queue = people.difference(stair1_queue)
            time1 = checkTime(
                stair1_queue, stair1[1], stair1[0][0], stair1[0][1])
            time2 = checkTime(
                stair2_queue, stair2[1], stair2[0][0], stair2[0][1])
            # tempRes = max(time1,time2)
            # if res < tempRes:
            #     res = tempRes