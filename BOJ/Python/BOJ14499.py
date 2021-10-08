import sys 
sys.stdin = open('BOJ14499.txt','r')
from pprint import pprint as pp 

N,M,x,y,k = map(int,input().split())
mat = [[*map(int,input().split())] for _ in range(N)]
orders = [*map(int,input().split())]
#  동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
dr = [0,(0,1),(0,-1),(-1,0),(1,0)]
now = x,y
# top, north, east, west, south, bottom 
dice = [0]*6

# 0 1 2 3 4 5
#east
# east -> bottom 
# bottom -> west 
# west -> top 
# top -> east 
#west 
# west -> bottom
# bottom -> east
# east -> top
# top -> west 
# north 
# north -> bottom
# bottom -> south
# south -> top
# top -> north
# south
# south -> bottom
# bottom -> north 
# north -> top
# top -> south 
def roll(order,dice):
    top, north, east, west, south, bottom = dice 
    temp = [0]*6
    if order == 1:
        temp[0] = west
        temp[1] = north
        temp[2] = top
        temp[3] = bottom
        temp[4] = south
        temp[5] = east 
    elif order == 2:
        temp[0] = east
        temp[1] = north
        temp[2] = bottom 
        temp[3] = top
        temp[4] = south
        temp[5] = west 
    elif order == 3:
        temp[0] = south
        temp[1] = top
        temp[2] = east
        temp[3] = west
        temp[4] = bottom
        temp[5] = north  
    elif order == 4:  
        temp[0] = north
        temp[1] = bottom
        temp[2] = east
        temp[3] = west
        temp[4] = top
        temp[5] = south  
    return temp 

def isMap(x,y):
    return 0 <= x < N and 0 <= y < M 

def move(order,now,dice):
    dx,dy = dr[order]
    nx,ny = now[0]+dx, now[1]+dy
    if isMap(nx,ny):
        dice = roll(order,dice)
        now = nx,ny

        if mat[nx][ny] == 0:
            mat[nx][ny] = dice[5]
        else:
            dice[5] = mat[nx][ny]
            mat[nx][ny] = 0
        print(dice[0])
        return now, dice
    else:
        return now,dice

for order in orders:
    now,dice = move(order,now,dice)

