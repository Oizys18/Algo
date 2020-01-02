import sys
sys.stdin = open('input2.txt','r')

for T in range(int(input())):
    N = int(input())
    mat = [[int(x) for x in input()] for _ in range(N)]
    
    res = 0 
    for x in range(N):
        if x < N//2:
            res += sum(mat[x][N//2-x : N//2 + (x+1)])
        elif x == N//2:
            res += sum(mat[x][:])
        elif x > N//2:
            res += sum(mat[x][N//2 - (N-x) +1 : N//2 + (N-(x+1)+1)])
    print("#{} {}".format(T+1,res))


"""
(N//2,N//2): 중간 
상하좌우 
(N//2, N//2 - 1)
(N//2, N//2 + 1)
(N//2 - 1, N//2)
(N//2 + 1, N//2)

"""

"""
가로 더하기 
-> 중간 : N 길이만큼 더함 

0:  0, N//2
1:  1, N//2-1  1,N//2   1,N//2 + 1
2:  2, N//2-2  1,N//2-1, 1,N//2  +1 , 1,N//2 + 2

...
N//2 : N//2, 0 ....................N//2,N-1  


N-1 : N-1, N//2-1   N-1,N//2    N-1 , N//2 +1 
N: N-1, N//2 
 
"""
    