import sys
sys.stdin = open('BOJ2580.txt','r')
from pprint import pprint as pp
#스도쿠
mat = [[*map(int,input().split())] for _ in range(9)]


for x in range(9):
    check = [0]*10
    empty = 0
    print(check)
    for y in range(9):
        print(mat[x][y])
        check[mat[x][y]] = 1 
        if not mat[x][y]:
            empty = (x,y)
    if sum(check) == 9:
        pp(mat)
        print(check)
        for c in range(9):
            if not check[c]:
                mat[empty[0]][empty[1]] = c
        pp(mat)