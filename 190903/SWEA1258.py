#SWEA1258

import sys
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    n = int(input())
    mat = [list(map(int,input().split())) for _ in range(n)]
    li = []
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if mat[x][y]:
                x1, y1 = x, y 
                while y < n-1:
                    if mat[x][y+1] == 0 or y == n - 1:
                        break
                    y += 1    
                while x < n-1:
                    if mat[x+1][y] == 0 or x == n - 1: 
                        break
                    x += 1    
                x2, y2 = x, y 
                li.append(((x2-x1+1)*(y2-y1+1),x2-x1+1,y2-y1+1))
                for a in range(x2-x1+1):
                    for b in range(y2-y1+1):
                        mat[x1+a][y1+b] = 0
                x, y = x1, y2+1
    sli = sorted(li)
    print("#{0} {1}".format(T+1,len(sli)),end=' ')
    for i in sli:
        print(i[1],end=' ')
        print(i[2],end=' ')
    print()

