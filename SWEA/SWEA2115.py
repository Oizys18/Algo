# 벌꿀채취 revisited 원트 성공 
# from pprint import pprint as pp
# import sys
# sys.stdin = open('2115.txt', 'r')


import itertools
def check(li1,li2,M,C):
    res1 = 0
    res2 = 0
    for k in range(1,M+1):
        for iter1 in itertools.combinations(li1,k):
            if sum(iter1) <= C:
                temp1 = 0
                for it1 in iter1:
                    temp1 += it1*it1
                if temp1 > res1:
                    res1 = temp1
        for iter2 in itertools.combinations(li2,k):
            if sum(iter2) <= C:
                temp2 = 0
                for it2 in iter2:
                    temp2 += it2*it2
                if temp2 > res2:
                    res2 = temp2
    return res1 + res2    

T = int(input())
for testcase in range(1, T+1):
    N, M, C = map(int, input().split())
    mat = [[*map(int, input().split())] for _ in range(N)]
    res = 0
    visit = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            # templi1 구하기
            if y+M-1 < N:
                templi1 = mat[x][y:y+M]
                for i in range(y,y+M):
                    visit[x][i] = 1
                # templi2 구하기
                for a in range(N):
                    for b in range(N):
                        if not visit[a][b] and b+M-1 < N:
                            templi2 = mat[a][b:b+M]
                            tempRes = check(templi1,templi2,M,C)
                            if tempRes > res:
                                res = tempRes
    print(f"#{testcase} {res}")
