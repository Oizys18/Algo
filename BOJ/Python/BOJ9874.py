import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ9874.txt', 'r')

N = int(input())
holes = [[*map(int,input().split())] for _ in range(N)]

def get_hole(hole):
    sx,sy = hole
    nx = 1000000000
    nxt_i = 0
    for i in range(N):
        a,b = holes[i]
        if sy == b and a > sx:
            if a < nx:
                nx = a
                nxt_i = i
    if nx == 1000000000:
        return 0 
    return nxt_i

def check(paired):
    for i in range(N):
        visit = [0]*N
        visit[i] = 1
        
        # 다음 웜홀 구하기 
        nxt_hole = get_hole(holes[i])
        while nxt_hole: 
            for x,y in paired:
                flag = 0 
                if nxt_hole == x:
                    if not visit[y]:
                        visit[y] = 1 
                        nxt_hole = get_hole(holes[y])
                    else:
                        flag = 1
                        break 
                elif nxt_hole == y:
                    if not visit[x]:
                        visit[x] = 1 
                        nxt_hole = get_hole(holes[x])
                    else:
                        flag = 1
                        break 
            if flag:
                break        
        if flag:
            return True 

answer=[]
def pair(k,visit,paired):
    if k == N//2 :
        if check(paired):
            answer.append(1)  
        return 
    else:
        for i in range(k,N):
            if not visit[i]:
                visit[i] = 1 
                for j in range(i,N):
                    if not visit[j]:
                        visit[j] = 1 
                        paired.append((i,j))
                        pair(k+1,visit,paired)
                        paired.pop()
                        visit[j] = 0 
                visit[i] = 0
pair(0,[0]*N,[])

print(sum(answer))