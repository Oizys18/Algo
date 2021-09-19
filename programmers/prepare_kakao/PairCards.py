"""
board는 4x4, 16칸 
카드는 최대 6쌍 

-> 지우는 순서는 최대 6! 가짓수 -> 720 
모든 케이스 순서대로 확인해봐도 된다.

"""
from collections import defaultdict
from itertools import permutations as perm 
from copy import deepcopy

    
def solution(board, r, c):
    answer = 0
    N = len(board)
    cards = defaultdict(list)
    for x in range(N):
        for y in range(N):
            if board[x][y]:
                cards[board[x][y]].append((x,y))
    def getDist(x1,y1,x2,y2,mat):
        q = []
        q.append((x1,y1,0))
        visit = [[0]*N for _ in range(N)]
        dist = 0
        while q:
            x,y,depth = q.pop(0)
            if (x,y)==(x2,y2):
                dist = depth
                break
            if x !=x2:1
                if x < x2:
                    nx = x+1
                elif x > x2: 
                    nx = x-1
                if mat[nx][y]:
                    if not visit[nx][y]:
                        visit[nx][y] = 1 
                        q.append((nx,y,depth+1))
                while x!=x2:
                    if x<x2:
                        nx = x+1
                    else: 
                        nx = x-1
                    if mat[nx][y]:
                        if not visit[nx][y]:
                            visit[nx][y] = 1 
                            q.append((nx,y,depth+1))
                        break 
                    else:x = nx
            if y !=y2:
                if y < y2: 
                    ny = y +1
                elif y > y2: 
                    ny = y -1 
                if mat[x][ny]:
                    if not visit[x][ny]:
                        visit[x][ny] = 1
                        q.append((x,ny,depth+1))   
                while y!=y2:
                    if y < y2: 
                        ny = y +1
                    else: 
                        ny = y -1 
                    if mat[x][ny]:
                        if not visit[x][ny]:
                            visit[x][ny] = 1
                            q.append((x,ny,depth+1))
                        break
                    else:y = ny 
        return dist

    mnTotal = 100
    for pattern in perm(cards.keys()):
        mat = deepcopy(board)
        patternTotal = 0
        for i,k in enumerate(pattern):
            (x1,y1),(x2,y2) = cards[k]
            patternTotal += getDist(r,c,x1,y1,mat)
            patternTotal += getDist(x1,y1,x2,y2,mat)
            patternTotal += 2
            r,c = x2,y2
            mat[x1][y1] = 0
            mat[x2][y2] = 0 
        mnTotal = min(mnTotal,patternTotal)
    print(mnTotal)
    return answer 

board= [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
print(solution(board,r,c))