"""
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
# 이진트리의 전위, 중위, 후위 순회 

# 트리의 모양 
a = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'




line = list(map(int,a.split()))
edges = {}
for i in range(len(line)):
    if line[i] not in edges.keys():
            edges[line[i]] = [0,0]
    if i % 2 == 0:
        if edges[line[i]][0]: 
            edges[line[i]][1] = line[i+1]
        else:
            edges[line[i]][0] = line[i+1]
visit =[0]*14
visit2 =[0]*14
visit3 =[0]*14
# 전위
def preorder(node):
    print(node,end=' ')
    if visit[node]:
        return
    else:
        visit[node] = 1
        if edges[node][0]:
            preorder(edges[node][0])
        if edges[node][1]:
            preorder(edges[node][1])
print('----전위----')
preorder(1)
print()

# 중위
def inorder(node):
    if visit2[node]:
        return
    else:
        if edges[node][0]:
            inorder(edges[node][0])
        print(node,end=' ')
        visit2[node] = 1
        if edges[node][1]:
            inorder(edges[node][1])
print('----중위----')
inorder(1)
print()


# 후위
def postorder(node):
    if visit3[node]:
        return
    else:
        if edges[node][0]:
            postorder(edges[node][0])    
        
        if edges[node][1]:
            postorder(edges[node][1])
        visit3[node] = 1
        print(node,end=' ')
print('----후위----')
postorder(1)
print()