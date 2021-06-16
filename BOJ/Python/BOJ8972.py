import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ8972.txt', 'r')

R,C = map(int,input().split())
mat = [input() for _ in range(R)]
moves = [int(i) for i in input()]
print(R,C)
pp(mat)
print(moves)

# 방향     1     2     3     4      5     6     7        8      9
dr = [0,(1,-1),(1,0),(1,1),(0,-1),(0,0),(0,1),(-1,-1),(-1,0),(-1,1)]

adu = set()
for x in range(R):
    for y in range(C):
        if mat[x][y] =='I':
            js = (x,y)
        elif mat[x][y] =='R':
            adu.add((x,y))
print('jongsu:',js)
print('aduino:',adu)

# 아두이노의 다음 움직임 계산
def next_move(r1,s1,r2,s2):
    far = 201
    save = (0,0)
    for dr,ds in dr:
        nr,ns = r2+dr, s2+ds
        if abs(nr-r1)+abs(ns-s1) < far:
            far = abs(nr-r1)+abs(ns-s1)
            save = (nr,ns)
    return save


while moves:
    move = moves.pop(0)
    js = (js[0] + dr[move][0], js[1]+ dr[move][1])

    check_collide = dict()
    for r2,s2 in adu:
        nr,ns = next_move(js[0],js[1],r2,s2)
        if not check_collide.get((nr,ns)):
            check_collide[(nr,ns)] = 0
        check_collide[(nr,ns)] += 1 
    new_adu = set()
    for k,v in check_collide.items:
        if v == 1:
            new_adu.add(k)
    # for ax,ay in new_adu:
    #     if (ax,ay) == js:


    