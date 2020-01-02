import sys
sys.stdin = open('input3.txt','r')

def DFS(node):
    global visit
    global res
    if len(visit) - 2 > res:
        return
    if len(edges[node]) == 0:
        if res >= len(visit)-2:
            res = len(visit)-2
        return
    else:
        for j in edges[node]:
            visit.append(j)
            DFS(j)
            visit.pop()

for T in range(int(input())):
    stops = list(map(int,input().split())) + [0]
    edges = {}
    N = stops[0]
    for stop in range(1, N + 1):
        if stop not in edges.keys():
            edges[stop] = []
        for i in range(1, stops[stop] + 1):
            if stop + i < N + 1:
                edges[stop].append(stop+i)
    res = N
    visit = [1]
    DFS(1)
    print("#{} {}".format(T+1,res))
