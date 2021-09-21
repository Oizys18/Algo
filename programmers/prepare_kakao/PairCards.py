"""
board는 4x4, 16칸 
카드는 최대 6쌍 

-> 지우는 순서는 최대 6! 가짓수 -> 720 
모든 케이스 순서대로 확인해봐도 된다.

"""
from pprint import pprint as pp
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
    def getDist(a,b,c,d,mat):
        # print(a,b,c,d,'--------')
        # pp(mat)
        q = []
        q.append((a,b,0))
        visit = [[0]*N for _ in range(N)]
        dist = 0
        while q:
            x,y,depth = q.pop(0)
            # print(x,y,depth,c,d)
            if x==c and y ==d :
                # print(x,y,c,d,q)
                dist = depth
                break
            if x !=c:
                if x < c:
                    nx = x+1
                elif x > c: 
                    nx = x-1
                if not visit[nx][y]:
                    visit[nx][y] = 1 
                    q.append((nx,y,depth+1))
                # ctrl x 
                nx = x 
                while nx!=c:
                    if nx<c:
                        nx += 1 
                    else: 
                        nx -= 1
                    if mat[nx][y] or nx == N-1 or nx==0:
                        if not visit[nx][y]:
                            visit[nx][y] = 1 
                            q.append((nx,y,depth+1))
                        break 
            
            if y !=d:
                if y < d: 
                    ny = y +1
                elif y > d: 
                    ny = y -1 
                if not visit[x][ny]:
                    visit[x][ny] = 1
                    q.append((x,ny,depth+1))   
                
                # ctrl y
                ny =  y
                while ny!=d:
                    if ny < d: 
                        ny += 1
                    else: 
                        ny -= 1 
                    if mat[x][ny] or ny==N-1 or ny == 0:
                        if not visit[x][ny]:
                            visit[x][ny] = 1
                            q.append((x,ny,depth+1))
                        break
                    
        return dist

    print(cards)
    mnTotal = 100
    for pattern in perm(cards.keys()):
        mat = deepcopy(board)
        patternTotal = 0
        a,b = r,c
        print(pattern,"pattern")
        for i,k in enumerate(pattern):
            (x1,y1),(x2,y2) = cards[k]
            print("a,b:",a,b)
            mv1 = getDist(a,b,x1,y1,mat)
            mv2 = getDist(a,b,x2,y2,mat)
            if mv1 < mv2:
                mvPrev = mv1
                mvNext = getDist(x1,y1,x2,y2,mat)
                a,b = x2,y2
            else:
                mvPrev = mv2
                mvNext = getDist(x2,y2,x1,y1,mat)
                a,b = x1,y1
                
            patternTotal += mvPrev + mvNext +2            
            print(x1,y1,x2,y2,':',mvPrev,mvNext)
            
            mat[x1][y1] = 0
            mat[x2][y2] = 0 
        print(patternTotal)
        mnTotal = min(mnTotal,patternTotal)
    print(mnTotal)
    return answer

board= 	[[0, 0, 1, 0], [1, 0, 0, 0], [4, 4, 3, 2], [0, 3, 2, 0]]
r = 2
c = 0
print(solution(board,r,c))
"""
(4, 3, 2, 1) pattern
a,b: 2 0
2 0 2 1 : 0 1
a,b: 2 1
2 2 3 1 : 1 2
a,b: 2 2
2 3 3 2 : 1 2 
a,b: 2 3
0 2 1 0 : 2 2



4 > 3 > 2 > 1 에서, (2,0) -> (2,1) , (3,1) -> (2,2)," (2,3)-> (3,2) ,  (0,2) -> (1,0)" 이렇게 진행해야함 
매번 가장 가까운 것만 선택하면 오히려 비효율이 발생할 수 있다. 
그런데 통과했네? ???????
이왜됨
19"""

"""
# 0 0 1 0   2,0
# 1 0 0 0   e > e        e > e 
# 4 4 3 2   > e < . e    . e > ^ e  
# 0 3 2 0   > e > ^ e    > e . < e 
#           ^ < e < . e  ^ e < . e  3 5 5 5 18 
"""