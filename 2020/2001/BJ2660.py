N = int(input())
mat = [[0]*(N+1) for _ in range(N+1)]
member = {}

def BFS(depth,node):
    queue = []
    visit = []
    queue.append((depth,node))
    maxDepth = 0
    while queue:
        depth,dot = queue.pop(0)
        if depth > maxDepth:
            maxDepth = depth
        if dot not in visit:
            visit.append(dot)
            if dot in member.keys():
                for i in member[dot]:
                    queue.append((depth+1,i))
    return (node, maxDepth-1) 

while True:
    a,b = map(int,input().split())
    if a == -1:
        break
    if a not in member.keys():
        member[a] = []
    if b not in member.keys():
        member[b] = []    
    member[a].append(b)
    member[b].append(a)

res = []
for i in member.keys():
    res.append(BFS(0,i))
result = []
people = []
for j in res:
    a,b = j
    result.append(b)
score = min(result)
count = result.count(score)
print("{0} {1}".format(score, count))
for k in res:
    a,b = k
    if b == score:
        people.append(a)
for l in sorted(people):
    print(l,end=' ')
print()