import sys
sys.stdin=open('input2.txt','r')

for T in range(int(input())):
    N,M,L = map(int,input().split())
    leaves = [0]*(N+1)
    for _ in range(M):
        node, leaf = map(int,input().split())
        leaves[node] = leaf
    temp = 0
    def solve(node):
        global temp
        if node*2 > N or leaves[node]:
            return
        else:
            solve(node*2)
            solve(node*2+1)
            if node*2 <= N:
                leaves[node] += leaves[node*2]
            if node*2+1 <= N:
                leaves[node] += leaves[node*2+1]

                 
    solve(1)
    print(f"#{T+1} {leaves[L]}")