# N과 M (1)
N, M = map(int, input().split())
visited = [0]*N
arr = range(1, N+1)
temp = [0]*M


def perm(k):
    if k == M:
        for t in temp:
            print(t, end=' ')
        print()
    else:
        for i in range(N):
            if visited[i]:
                continue
            temp[k] = arr[i]
            visited[i] = 1
            perm(k + 1)
            visited[i] = 0


perm(0)
