import sys
sys.stdin= open('input.txt','r')


def check(node):
    global cnt 
    if visit[node]:
        return 

    else:
        for j in edges[node]:
            check(j)
            visit[j] = 1
            cnt += 1


for T in range(int(input())):
    E, N = map(int,input().split())
    edges = {}
    li = list(map(int,input().split()))
    cnt = 1
    
    for i in range(len(li)):
        if li[i] not in edges.keys():
            edges[li[i]] = []
        if not i%2:
            edges[li[i]].append(li[i+1])
    visit = [0] * (max(edges.keys()) + 1)        
    check(N)
    print(f"#{T+1} {cnt}")
