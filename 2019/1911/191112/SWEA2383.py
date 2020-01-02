# 계단 내려가기 
import sys
from pprint import pprint as pp
sys.stdin = open('1949.txt','r')
T = int(input())
for testcase in range(T):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    tempMat = [[0]*N for _ in range(N)]
    stairs = []
    stairTime = []
    people = []
    # Find people and stairs
    for r in range(N):
        for c in range(N):
            if 2 <= mat[r][c] <= 10:
                stairs.append((r,c))
                stairTime.append(mat[r][c])
            if mat[r][c] == 1:
                people.append((r,c))
    
    # calc movement time
    def far(r,c,stair):
        sr, sc = stairs[stair]
        return abs(r-sr) + abs(c-sc)
    
    # go Down 
    def down(arr, depth):
        time = 0
        upstair = [0,0,0]
        downstair = [0,0,0]
        while True:
            for k in range(len(downstair)):
                if downstair[k]:
                    downstair[k] -= 1

            for j in range(len(upstair)):
                if upstair[j]:
                    if upstair[j] == time:
                        if 0 in downstair:
                            downstair[downstair.index(0)] = depth 
                            upstair[j] = 0
                        else:
                            upstair[j] += 1

            for i in range(len(arr)):
                if arr[i]:
                    if arr[i] == time:
                        if 0 in upstair:
                            upstair[upstair.index(0)] = time + 1
                            arr[i] = 0
                        else:
                            arr[i] += 1
            if sum(arr) == 0 and sum(upstair) == 0 and sum(downstair) == 0:
                return time
            time += 1

    # choice of stairs
    resTime = 100
    for i in range(2 ** len(people)): 
        stairChoice = [0 for _ in range(len(people))]
        for j in range(len(people)):
            if i & (1 << j):
                stairChoice[j] = 0
            else:
                stairChoice[j] = 1     
        timeSchedule = []
        for i in range(len(people)):
            r,c = people[i]
            stair = stairChoice[i]
            timeSchedule.append((far(r,c,stair),stair))
        firS = []
        secS = []
        for time, stair in timeSchedule:
            if stair == 0:
                firS.append(time)
            else:
                secS.append(time)
        
        thisTime = max(down(firS, stairTime[0]),down(secS, stairTime[1]))
        if resTime >= thisTime:
            resTime = thisTime
    print(f"#{testcase+1} {resTime}")