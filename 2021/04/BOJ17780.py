# 새로운 게임
import sys
sys.stdin = open('BOJ17780.txt','r')
from pprint import pprint as pp 
from collections import defaultdict
from heapq import * as heapq

# input
N,K = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
pp(mat)

# 위 아래 왼 오른
mv = {
    1: (-1,0),
    2: (1,0),
    3: (0,1),
    4: (0,-1)
}
pp(mv)

# 말 위치 정보
move = {k:list(map(int,input().split())) for k in range(K)}
pp(move)

# 다음 칸 정보 확인 
def check_next (nx,ny):
    if 0 <= nx <= N and 0 <= ny <= N:
        if mat[nx][ny] == 0:
            # 하양
            pass
        elif mat[nx][ny] ==1:
            # 빨강
            pass
        elif mat[nx][ny] == 2:
            # 파랑
            pass

    # 맵 밖으로 나감 
    else:return False

# 말 위치 정보 


# 풀이 
def solve():
    return 

