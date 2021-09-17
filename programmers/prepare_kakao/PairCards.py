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
    def getDist(x1,y1,x2,y2,mat) -> int:
        # return dist 
        pass

    def ctrlY(x1,y1,y2,mat):
        if y1 < y2:
            for i in range(y1+1,N):                
                if mat[x1][i]:
                    return x1,i
            return x1,N-1
        else:
            for i in range(y2-1,0,-1):
                if mat[x1][i]:
                    return x1,i
            return x1,0
    def ctrlX(y1,x1,x2,mat):
        if x1<x2:
            for i in range(x1+1,N):
                if mat[i][y1]:
                    return i,y1
            return N-1,y1
        else:
            for i in range(x2-1,0,-1):
                if mat[i][y1]:
                    return i,y1
            return 0,y1
        
    mnTemp = 100
    for pattern in perm(cards.keys()):
        mat = deepcopy(board)
        patternTotal = 0
        for k in pattern:
            (x1,y1),(x2,y2) = cards[k]
            patternTotal += getDist(x1,y1,x2,y2,mat)
            mat[x1][y1] = 0
            mat[x2][y2] = 0 
        mnTemp = min(patternTotal,mnTemp)
    
    return answer