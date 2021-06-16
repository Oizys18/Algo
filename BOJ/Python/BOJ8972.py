import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ8972.txt', 'r')

R,C = map(int,input().split())
mat = [[0 if i =='.' else 1 if i =='R' else 2 for i in input()] for _ in range(R)]
moves = [int(i) for i in input()]


# 방향     1     2     3     4      5     6     7        8      9
dr = [(1,-1),(1,0),(1,1),(0,-1),(0,0),(0,1),(-1,-1),(-1,0),(-1,1)]

adu = set()
for x in range(R):
    for y in range(C):
        if mat[x][y] == 2:
            js = (x,y)
        elif mat[x][y] == 1:
            adu.add((x,y))


# 아두이노의 다음 움직임 계산
def next_move(r1,s1,r2,s2):
    far = 201
    save = (0,0)
    for dx,dy in dr:
        nr,ns = r2+dx, s2+dy
        if abs(nr-r1)+abs(ns-s1) < far:
            far = abs(nr-r1)+abs(ns-s1)
            save = (nr,ns)
    return save

turn = 1
while moves:
    move = moves.pop(0)
    mat[js[0]][js[1]] = 0 
    js = (js[0] + dr[move-1][0], js[1]+ dr[move-1][1])
    mat[js[0]][js[1]] = 2
    check_collide = dict()
    for r2,s2 in adu:
        nr,ns = next_move(js[0],js[1],r2,s2)
        if not check_collide.get((nr,ns)):
            check_collide[(nr,ns)] = 0
        check_collide[(nr,ns)] += 1 
        mat[r2][s2] = 0
    flag = 0
    new_adu = set()
    for k,v in check_collide.items():
        if k == js:
            print(f'kraj {turn}')
            flag = 1
            break
        if v == 1:
            new_adu.add(k)
    if flag:
        break
    
    for nr,ns in new_adu:
        mat[nr][ns] = 1
    
    adu = new_adu
    turn += 1

if not flag:
    for x in range(R):
        line = ''
        for y in range(C):
            if mat[x][y] == 0:
                line += '.'
            elif mat[x][y] == 1:
                line += 'R'
            elif mat[x][y] == 2:
                line += 'I'
        print(line)
