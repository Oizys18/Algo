# 단면의 모든 세로방향에 대해서 동일한 특성의 셀들이
# K개 이상 연속적으로 있는 경우에만 성능검사를 통과하게 된다.

<<<<<<< HEAD
from pprint import pprint as pp

# 함수

import copy
def check(y, K, temp):
    cnt = 1
    x = 0
    medi = temp[0][y]
    while True:
        if cnt == K:
            return True
        x += 1
        if x < D:
            if temp[x][y] == medi:
                cnt += 1
            else:
                medi = temp[x][y]
=======
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
>>>>>>> 4ab1a72bc22b0a7fe22cc24442839ccc15d372fe
                cnt = 1
        else:
            return False

<<<<<<< HEAD

def solve(depth, mat, cnt):
    global res
    if cnt >= res:
        return
    if depth >= D:
        return    
    else:
        checkCNT = 0
        for i in range(W):
            checkCNT += check(i, K, mat)

        if checkCNT != W:
            # 색칠 안함
            solve(depth+1, mat, cnt)

            temp = copy.deepcopy(mat)

            # 0으로 칠함
            temp[depth] = [0]*W
            solve(depth+1, temp, cnt+1)
            # 1로 칠함
            temp[depth] = [1]*W
            solve(depth+1, temp, cnt+1)
        else:
            if res > cnt:
                res = cnt
                return


T = int(input())
for testcase in range(T):
    D, W, K = map(int, input().split())
    mat = [[*map(int, input().split())] for _ in range(D)]
    paint = [0]*(D+1)
    res = K
    solve(0,mat,0)

    print(f"#{testcase+1} {res}")

=======
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
    
>>>>>>> 4ab1a72bc22b0a7fe22cc24442839ccc15d372fe


"""
1         
6 8 3         
1 1 1 1 0 0 1 0
0 0 1 1 0 1 0 1
1 1 1 1 0 0 1 0
1 1 1 0 0 1 1 0
1 1 0 1 1 1 1 0
1 1 1 0 0 1 1 0
"""

"""
10
6 8 3
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1
6 8 3
1 1 1 1 0 0 1 0
0 0 1 1 0 1 0 1
1 1 1 1 0 0 1 0
1 1 1 0 0 1 1 0
1 1 0 1 1 1 1 0
1 1 1 0 0 1 1 0
6 8 4
1 1 0 0 0 1 1 0
1 0 1 0 0 1 1 1
0 1 0 0 1 1 0 0
1 0 1 0 0 0 0 0
1 1 0 0 0 0 0 0
1 0 0 0 1 1 1 1
6 4 4
1 1 0 0
0 1 0 1
0 0 0 1
1 1 1 1
1 1 0 1
1 0 1 0
6 10 3
0 1 0 0 0 1 0 0 1 1
0 1 1 0 0 1 0 0 1 0
0 1 0 0 1 0 1 1 1 1
0 0 0 0 0 1 1 1 1 0
0 1 0 0 1 1 1 1 1 1
1 0 0 0 1 1 0 0 1 1
6 6 5
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
6 6 4
1 1 1 1 1 1
0 0 0 0 0 1
0 1 1 1 0 1
0 1 0 1 0 1
0 1 0 0 0 1
0 1 1 1 1 1
8 15 3
0 1 1 0 0 1 1 0 1 1 0 0 0 0 0
1 0 0 0 1 1 0 0 0 0 0 1 0 1 1
1 1 0 1 0 1 0 1 0 1 0 1 0 0 0
0 1 1 1 0 0 1 0 0 0 0 1 0 0 0
0 0 0 0 0 0 1 0 0 0 1 1 0 0 1
1 0 1 0 0 1 0 1 1 1 1 0 1 1 1
0 0 0 0 0 1 1 1 0 0 0 0 0 1 0
0 0 1 0 1 1 0 1 1 0 0 0 1 0 0
10 20 4
1 0 1 1 1 1 1 1 1 1 0 0 1 1 1 0 1 1 0 1
1 1 0 1 1 1 0 0 1 0 0 0 1 1 1 1 0 0 1 0
1 1 0 1 1 0 0 0 1 1 1 1 1 0 0 1 1 0 1 0
0 0 0 1 1 0 0 0 0 1 0 0 1 0 1 1 1 0 1 0
0 1 1 0 1 0 1 0 1 0 0 1 0 0 0 0 1 1 1 1
1 0 1 0 1 0 1 1 0 0 0 0 1 1 1 0 0 0 0 0
0 1 0 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 1 1
1 0 0 0 0 1 0 1 1 0 1 1 0 1 0 0 1 1 1 0
0 1 1 0 0 1 0 1 0 0 0 0 0 0 0 1 1 1 0 1
0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 0 1 0
13 20 5
1 1 0 1 0 0 0 1 1 1 1 0 0 0 1 1 1 0 0 0
1 1 1 1 0 1 0 1 0 0 0 0 1 0 0 0 0 1 0 0
1 0 1 0 1 1 0 1 0 1 1 0 0 0 0 1 1 0 1 0
0 0 1 1 0 1 1 0 1 0 0 1 1 0 0 0 1 1 1 1
0 0 1 0 0 1 0 0 1 0 0 0 0 1 0 0 0 0 1 1
0 0 1 0 0 0 0 0 0 0 0 0 1 1 1 0 0 1 0 1
0 0 0 1 0 0 0 0 0 0 1 1 0 0 0 1 0 0 1 0
1 1 1 0 0 0 1 0 0 1 1 1 0 1 0 1 0 0 1 1
0 1 1 1 1 0 0 0 1 1 0 1 0 0 0 0 1 0 0 1
0 0 0 0 1 0 1 0 0 0 1 0 0 0 0 1 1 1 1 1
0 1 0 0 1 1 0 0 1 0 0 0 0 1 0 1 0 0 1 0
0 0 1 1 0 0 1 0 0 0 1 0 1 1 0 1 1 1 0 0
0 0 0 1 0 0 1 0 0 0 1 0 1 1 0 0 1 0 1 0
"""