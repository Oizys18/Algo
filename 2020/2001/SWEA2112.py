# 단면의 모든 세로방향에 대해서 동일한 특성의 셀들이 
# K개 이상 연속적으로 있는 경우에만 성능검사를 통과하게 된다.

from pprint import pprint as pp 
import itertools 

# 함수
def check(y):
    cnt = 1
    x = 0
    medi = mat[0][y]
    while True:
        if cnt == 3:
            return True
        x += 1
        if x < D:
            if mat[x][y] == medi:
                cnt += 1 
            else:
                medi = mat[x][y]
                cnt = 1
        else:
            return False

T = int(input())
for testcase in range(1):
    D,W,K = map(int,input().split())
    mat = [[*map(int,input().split())] for _ in range(D)]
    # rotMat = [*zip(*mat)]
    checkRes = 0
    for y in range(W):
        checkRes += check(y)
    if checkRes != W:
        # 최대 K 만큼 약을 넣는다. 
        for i in range(1,K+1):
            for line in itertools.combinations(range(1,W+1),i):
                # line 행에 i 만큼 약을 부어본다. 
                for j in range(1,i+1):
    


"""
1         
6 8 3         
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1
"""