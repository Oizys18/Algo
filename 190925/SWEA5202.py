# SWEA 5202

import sys
sys.stdin=open('input4.txt','r')

def DFS(node):
    global res
    if len(move[node]) == 0:
        res.append(len(visit))
        return
    else:
        if move[node]:
            for i in move[node]:
                visit.append(i)
                DFS(i)
                visit.pop()

for T in range(int(input())):
    N = int(input())
    times=[]
    for _ in range(N):
        s, e = map(int,input().split())
        times.append((s,e))
    arr =sorted(times)
    move = {}

    for i in range(N):
        move[i] = []
        for j in range(N):
            if arr[j][0] >= arr[i][1]:
                move[i].append(j) 
    result = 0
    res = []
    for k in range(N):
        visit = [k]
        DFS(k)
    print("#{} {}".format(T+1, max(res)))
    #     if res > result:
    #         result = res
    # print(result)






    # result = 0
    # for k in range(N):
    #     sR = stack(arr[k])
    #     res = len(sR)
    #     if res > result:
    #         print(sR)
    #         result = res
    # print(result)
