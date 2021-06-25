import sys
sys.stdin = open('BOJ2580.txt','r')
from pprint import pprint as pp
#스도쿠
mat = [[*map(int,input().split())] for _ in range(9)]
turned = list(map(list,zip(*mat)))

zeros = []
for x in range(9):
    for y in range(9):
        if mat[x][y] ==0:
            zeros.append((x,y))

def getGroup(x,y):
    return (x//3)*3 + (y//3)

def get_missing(x,y):
    g = getGroup(x,y)
    missing = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        if mat[x][i] in missing:
            missing.remove(mat[x][i])
        if mat[i][y] in missing:
            missing.remove(mat[i][y])
    for i in range(x//3*3,(x//3+1)*3):
        for j in range(y//3*3,(y//3+1)*3):
            if mat[i][j] in missing:
                missing.remove(mat[i][j])
    return missing

flag = 0

def solve(k):    
    global flag
    if flag:
        return
    if k == len(zeros):
        for x in range(9):
            for y in range(9):
                print(mat[x][y],end=' ')
            print('')
        flag = 1 
        return
    else:
        x,y = zeros[k]
        for found in get_missing(x,y):
            mat[x][y] = found
            solve(k+1)
            mat[x][y] = 0
solve(0)


"""
#첫번째 풀이
mat = [[*map(int,input().split())] for _ in range(9)]
turned = list(map(list,zip(*mat)))

zeros = set()
for x in range(9):
    for y in range(9):
        if mat[x][y] ==0:
            zeros.add((x,y))
ten = {0,1,2,3,4,5,6,7,8,9}

while zeros:
    delete = set()
    for x,y in zeros:
        check = set()
        tcheck = set()
        zero = -1
        tzero = -1
        for i in range(9):
            if mat[x][i]:
                check.add(mat[x][i])
            if turned[y][i]:
                tcheck.add(turned[y][i])

        check = ten-check
        if len(check) == 1:
            delete.add((x,y))
            mat[x][y] = turned[y][x] = check.pop()

        if not mat[x][y]:
            tcheck = ten-tcheck
            if len(tcheck) == 1:
                delete.add((x,y))
                mat[x][y] = turned[y][x] = tcheck.pop()
        

        if not mat[x][y]:
            if 0 <= x <3:
                nx = 0
            elif 3 <= x <6:
                nx = 3
            elif 6 <= x <9:
                nx = 6
            if 0 <= y <3:
                ny = 0
            elif 3 <= y <6:
                ny = 3
            elif 6 <= y <9:
                ny = 6

            scheck = set()
            szero = -1
            for a in range(3):
                for b in range(3):
                    if mat[nx+a][ny+b]:
                        scheck.add(mat[nx+a][ny+b])
            scheck = ten-scheck
            if len(scheck) == 1:
                delete.add((x,y))
                mat[x][y] = turned[y][x] = scheck.pop()
        
    zeros = zeros - delete 
"""

"""두번째
잘 만든 것 같긴함. 그런데 해답이 2개 이상 되는 경우 생각안함 
결국 백트래킹도 아님! 

mat = [[*map(int,input().split())] for _ in range(9)]
turned = list(map(list,zip(*mat)))

zeros = set()
for x in range(9):
    for y in range(9):
        if mat[x][y] ==0:
            zeros.add((x,y))
ten = {0,1,2,3,4,5,6,7,8,9}

while zeros:
    delete = set()
    for x,y in zeros:
        g = getGroup(x,y)
        missing = 0
        if len(ten-garo[x]) == 1:
            missing = (ten-garo[x]).pop()
        elif len(ten-sero[y]) == 1:
            missing = (ten-sero[y]).pop()
        elif len(ten-nemo[g]) == 1:
            missing = (ten-nemo[g]).pop()
        # else:

        if missing:    
            nemo[g].add(missing)
            garo[x].add(missing)
            sero[y].add(missing)
            mat[x][y] = missing

        delete.add((x,y))


    zeros = zeros-delete
"""