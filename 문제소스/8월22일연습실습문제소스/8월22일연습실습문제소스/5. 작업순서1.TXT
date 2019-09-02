import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    V, E = map(int, input().split())
    G = [[0] * (V + 2) for _ in range(V + 2)] # G[x][0] 진입차수 G[x][1] 진출 차수
    stack = [0] * 1000
    top = -1

    edges = list(map(int, input().split()))
    for i in range(E):
        u, v = edges[i*2: i*2 + 2]
        G[u][1] += 1
        G[u][G[u][1]+1] = v
        G[v][0] += 1

    for i in range(1, V + 1):
        if G[i][0] == 0:
            top += 1
            stack[top] = i

    print("#%d"%tc, end=' ')

    while top != -1:
        x = stack[top]
        top -= 1
        print("%d"%x, end=' ')
        for i in range(G[x][1]):
            G[G[x][2 + i]][0] -= 1
            if G[G[x][2 + i]][0] == 0:
                top += 1
                stack[top] = G[x][2 + i]

    print()

