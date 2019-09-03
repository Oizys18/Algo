#SWEA1258

import sys
sys.stdin = open('input2.txt','r')

for T in range(int(input())):
    n = int(input())
    mat = [list(map(int,input().split())) for _ in range(n)]
    li = []
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if mat[x][y]:
                x1, y1 = x, y 
                while y < n-1:
                    y += 1
                    if mat[x][y] == 0 or y == n - 1:
                        y -= 1
                        break
                while x < n-1:
                    x += 1
                    if mat[x][y] == 0 or x == n - 1:
                        x -= 1 
                        break
                x2, y2 = x, y 
                li.append((x1,y1,x2,y2))
                for x in range(x2-x1+1):
                    for y in range(y2-y1+1):
                        mat[x1+x][y1+y] = 0
    print(li)
    print(mat)
             
