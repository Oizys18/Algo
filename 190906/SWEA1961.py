# SWEA1961

for T in range(int(input())):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    mat1 = list(zip(*mat))
    mat2 = []
    for i in mat:
        mat2 = list(reversed(i)) + mat2 
    print(mat2)


"""
1
3
1 2 3
4 5 6
7 8 9
"""