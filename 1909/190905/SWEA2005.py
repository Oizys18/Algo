import sys
sys.stdin = open('input2.txt','r')

def pa(n):
    if n == 1:
        return [[1]]
    base = [[1],[1,1]]
    base.extend([[] for _ in range(n-2)]) 
    for i in range(2,n):
        for j in range(len(base[i-1])-1):
            base[i].append(base[i-1][j]+base[i-1][j+1])
        base[i] = [1] + base[i] + [1]
    return base

for T in range(int(input())):
    N = int(input())
    print("#{}".format(T+1))
    for i in pa(N):
        for j in i:
            print(j,end=' ')
        print()
    # print(pa(N))
