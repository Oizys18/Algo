import sys
sys.stdin = open("input.txt", "r")

def DFSr(v):
    for i in range(cnt[v]):
        if visited[G[v][i]] == 0 : DFSr(G[v][i])

    visited[v] = 1
    print("%d" % v, end=' ')

for tc in range(1, 11):
    V, E = map(int, input().split())
    G = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    cnt = [0] * (V + 1)

    edges = list(map(int, input().split()))
    for i in range(E):
        u, v = edges[i*2: i*2 + 2]
        G[v][cnt[v]] = u
        cnt[v] += 1

    print("#%d"%tc, end=' ')

    for i in range(1, V+1):
        if visited[i] == 0:
            DFSr(i)

    print()