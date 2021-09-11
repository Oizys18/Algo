from math import inf 
def solution(n, s, a, b, fares):
    mat = [[inf]*n for _ in range(n)]
    for c,d,f in fares:
        mat[c-1][d-1] = f
        mat[d-1][c-1] = f 
    for x in range(n):
        for y in range(n):
            if x == y:
                mat[x][y] = 0 
    
    for k in range(n):
        mat[k][k] = 0
        for x in range(n):
            for y in range(x,n):
                if x !=y:
                    temp = min(mat[x][y],mat[x][k]+mat[k][y])
                    mat[x][y] = mat[y][x] = temp 
    mn = inf
    for k in range(n):
        mn = min(mat[s-1][k] + mat[k][a-1]+mat[k][b-1],mn)
    return mn

"""
이중 플로이드 와샬,

line 15에서 행렬 우상단 ( 대각선으로 잘랐을 때 x==y를 기준으로 완전히 대칭이다.)을 계산안하도록 y의 범위를 x,n으로 잡아주지 않으면 시간초과가 발생한다. 
"""