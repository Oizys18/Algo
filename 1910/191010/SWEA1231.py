import sys

sys.stdin = open('input.txt','r')

def inorder(node):
    if visit[node]:
        return
    else:
        if edges[node][0]:
            inorder(edges[node][0])
        print(words[node],end='')
        visit[node] = 1
        if edges[node][1]:
            inorder(edges[node][1])

for T in range(1,11):
    edges = {}
    length = int(input())
    words = [0]*(length+1)
    visit = [0]*(length+1)
    
    for i in range(length):
        line = input().split()
        node = int(line[0])
        edges[node] = [0,0]
        words[node] = line[1]
        if len(line) > 2:
            edges[node][0] = int(line[2])
        if len(line) > 3:
            edges[node][1] = int(line[3])
    print(f'#{T} ',end='')
    inorder(1)
    print()
