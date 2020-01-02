# SWEA 1238 Contact 

"""
from to ... 반복 input

1. 행렬로 input 입력 
2. BFS 구현
2-1 queue에 (depth,adjnode)
3-1 depth 가장 깊은 것 출력 
"""
import sys
sys.stdin = open('input.txt','r')

def BFS(depth,start):
    queue = []
    visited = []
    called = []
    queue.append((depth,start))
    while queue:
        depth, node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            called.append((depth,node))
            maxDep = depth
            if node in contact.keys():
                for n in contact[node]:
                    queue.append((depth+1,n))
    return called,maxDep


for tc in range(1,11):
    T,start = map(int,input().split())
    line = list(map(int,input().split()))
    contact = {}
    for i in range(0,len(line),2):
        if line[i] not in contact.keys():
            contact[line[i]] = []
        if line[i] in contact.keys():
            contact[line[i]].append(line[i+1])
    calls,d = BFS(0,start)
    res_li = [i for i in calls if i[0]==d]
    res = 0
    for i in res_li:
        if i[1] > res:
            res = i[1]
    print("#{0} {1}".format(tc,res))