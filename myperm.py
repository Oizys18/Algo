arr = [1,1,3,4,5]
N = len(arr)

# visited = [0]*(N+1)
# def perm(k, s):
#     # print(s)  
#     if visited[k]:
#         return
#     visited[k] = 1
      
#     if k == N:
#         return
#     else:
#         s.append(arr[k])
#         perm(k+1, s)
#         s.pop()
#         perm(k+1, s)

# perm(0,[])



visited = [[0]*(sum(arr)+1) for _ in range(N+1)]
def perm(k, s):
    if visited[k][s]:
        return
    visited[k][s] = 1
    if k == N:
        return
    else:
        perm(k+1, s)
        perm(k+1, s + arr[k])

perm(0,0)
print(visited)