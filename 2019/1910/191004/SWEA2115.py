import sys
sys.stdin = open('input.txt','r')
from pprint import pprint as pp


# code 
import itertools

for T in range(int(input())):
    N, M, C = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    result = 0
    tempA = 0
    tempB = 0
    resA = 0
    resB = 0
    for x in range(N):
        for y in range(N-M+1):
            A = mat[x][y:y+M]
            for k in range(M):
                visit[x][y+k] = 1
            for ra in range(1, M + 1):
                for combA in itertools.combinations(A, ra):
                    if sum(combA) > C:
                        continue
                    else:
                        for ia in combA:
                            tempA += ia**2
                        if tempA > resA:
                            resA = tempA
                    tempA = 0

            for a in range(N):
                for b in range(N-M+1):
                    for k in range(M):
                        if visit[a][b+k]:
                            break
                    else:
                        B = mat[a][b:b+M] 
                        for rb in range(1, M + 1):
                            for combB in itertools.combinations(B, rb):
                                if sum(combB) > C:
                                    continue
                                else:
                                    for ib in combB:
                                        tempB += ib**2
                                    if tempB > resB:
                                        resB = tempB
                                tempB = 0
            if resA + resB > result:
                result = resA + resB
            resA = 0
            resB = 0
            visit = [[0]*N for _ in range(N)]
    print(f"#{T+1} {result}")

