# BJ2549 루빅의 사각형

import sys
from pprint import pprint
sys.stdin = open('input.txt','r')

cnt = 0

# 오른쪽으로 움직이는 함수, x 행을 n번 움직인다. 
def moveR(x,n):
    global cnt
    tempX = mat[x]
    cnt += n
    for i in range(4):
        tempX[i] = mat[x][x+n % 4]
        if x + n < 4:
            tempX[i] = mat[x][x+n]
        elif x + n >= 4:
            tempX[i] = mat[x][x+n-4]

# 아랫쪽으로 움직이는 함수, y 열을 n번 움직인다.  
def moveD(x,y,n):
    global cnt
    tempY = [mat[x][y],]

    pass


mat = [list(map(int,input().split())) for _ in range(4)]
mat2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
temp = {}
temp2 = [[(0,0)]*4 for _ in range(4)]
for x in range(4):
    for y in range(4):
        temp[mat2[x][y]] = (x,y)
print(temp)

for x in range(4):
    for y in range(4):
        if mat[x][y] != mat2[x][y]:
            x2, y2 = temp[mat[x][y]]
            print(mat[x][y],x,y)
            dx = 0
            dy = 0
            if x2 > x:
                dx = x2-x
            elif x > x2:
                dx = 4 - (x - x2)
            if y2 > y:
                dy = y2-y
            elif y > y2:
                dy = 4 - (y - y2)
            temp2[x][y] = (dx,dy)
pprint(temp2)



"""
for x in range(4):
    for y in range(4):
        if mat[x][y] != mat2[x][y]:
            x2, y2 = temp[mat[x][y]]
            # print(mat[x][y],(x,y),temp[mat[x][y]])
            dx = 0
            dy = 0
            if x2 > x:
                dx = x2-x
            elif x > x2:
                dx = 4 - (x - x2)
            if y2 > y:
                dy = y2-y
            elif y > y2:
                dy = 4 - (y - y2)
            temp2[x][y] = (dx,dy)
 
pprint(temp2)
mv = []
for x in range(4):
    for y in range(4):
        if temp2[x][y]:
            print(mv)
            a,b = temp2[x][y]
            if a:
                pprint(temp2)
                do = 1
                # print(a,b)
                for i in range(4):
                    c,d = temp2[i][y]
                    if a == c:
                        do = 1
                    else:
                        do = 0
                if do:
                    mv.append((2, y+1, a))
                    for j in range(4):
                        e,f = temp2[j][y]
                        if f:
                            # print((a+j) % 4)
                            temp2[j][y] = 0
                            temp2[(a + j) % 4][y] = (0,f)
                        else:
                            temp2[j][y] = 0
                # print(mv)
                # print(temp2)
            elif b:
                pprint(temp2)
                do = 1
                for l in range(4):
                    x3,y3 = temp2[x][l]
                    if b == y3:
                        do = 1
                    else:
                        do = 0
                if do:
                    mv.append((1, x+1, b))
                    for k in range(4):
                        g,h = temp2[x][k]
                        if g:
                            temp2[x][k] = 0 
                            temp2[x][(b+k) % 4] = (g,0)
                        else:
                            temp2[x][k] = 0
                        # temp2[x][k] = (g,0)

print(len(mv))
for move in mv:
    for m in move:
        print(m,end=' ')
    print()
"""