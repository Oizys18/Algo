# 점심식사
from pprint import pprint as pp
import sys
sys.stdin = open('2383.txt', 'r')


import itertools
def checkTime(stair_queue, stair_length, x, y):
    timeLi = []
    for a, b in stair_queue:
        timeLi.append(abs(a-x) + abs(b-y))
    timeLi.sort()

    time = 1
    stair_q = []
    down_q = []
    down = 0
    while True:
        delCnt3 = 0
        for d in range(len(down_q)):
            down_q[d] -= 1
            if down_q[d] <= 0:
                delCnt3 += 1
        for _ in range(delCnt3):
            down_q.pop(0)


        # 계단 진입 
        delCnt = 0
        for q in range(len(stair_q)):
            if stair_q[q] == stair_length and len(down_q) < 3:
                down_q.append(stair_length)
                delCnt += 1
            elif stair_q[q] > stair_length:
                stair_q[q] -= 1                

        for _ in range(delCnt):
            stair_q.pop(0)

        # 계단 위로 이동
        delCnt2 = 0
        for p in range(len(timeLi)):
            if timeLi[p]:
                if timeLi[p] <= time and len(stair_q) < 3:
                    stair_q.append(stair_length+1)
                    delCnt2 += 1
        for _ in range(delCnt2):
            timeLi.pop(0)
        
        if len(timeLi) == 0 and len(stair_q) == 0 and len(down_q) == 0:
            return time - 1
        time += 1



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

            tempRes = max(time1,time2)
            if res > tempRes:
                res = tempRes
    print(f"#{testcase} {res}")

"""
1
5
0 1 1 0 0
0 0 1 0 3
0 1 0 1 0
0 0 0 0 0
1 0 5 0 0
"""