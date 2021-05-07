"""
D[i][j] = 선분 (i,j)의 가중치
출력: 모든 쌍 최단 경로의 거리를 저장한 2-d 배열 D
"""
N = 5
D = [[0]*N for _ in range(N)]

def AllPairsShortest(D):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][k] + D[k][j], D[i][j])
    return D 