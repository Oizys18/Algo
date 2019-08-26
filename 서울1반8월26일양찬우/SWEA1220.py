#SWEA1220 Magnetic
import sys
sys.stdin = open('input.txt','r')

def _N(r,c):
    while True:
        if r == N-1:
            mat[r][c] = 0
            break
        elif mat[r+1][c] != 0:
            break

        if r < N-1 and mat[r+1][c] == 0:
            while r < N-1 and mat[r+1][c] == 0:
                mat[r][c],mat[r+1][c] = mat[r+1][c], mat[r][c]
        
def _S(r,c):
    while True:
        if r == 0:
            mat[r][c] = 0
            break
        elif mat[r-1][c] != 0:
            break
        if r > 0 and mat[r-1][c] == 0:
            while r > 0 and mat[r-1][c] == 0:
                mat[r][c],mat[r-1][c] = mat[r-1][c], mat[r][c]
    

for T in range(1,11):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    for _ in range(N):
        for r in range(len(mat)):
                for c in range(len(mat[r])):
                    # N극일 때 
                    if mat[r][c] == 1:
                        _N(r,c)
                    # S극일 때
                    elif mat[r][c] == 2:
                        _S(r,c)
    result = 0
    mat2 = list(zip(*mat))
    for i in mat2:
        stack = [0]
        temp = list(i)
        while len(temp):
            node = temp.pop()
            if node != stack[-1]:
                stack.append(node)
        result += stack.count(1)

    print("#{0} {1}".format(T,result))
