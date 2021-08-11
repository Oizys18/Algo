import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ5827.txt', 'r')

# inputs
N,M = map(int,input().split())
mat = [input() for _ in range(N)]
# variables 
answer = 0
gravity = True

for x in range(N):
    for y in range(M):
        if mat[x][y] == 'C':
            captain = (x,y)
        elif mat[x][y] == 'D':
            doctor = (x,y)
            
print(captain)
print(doctor)

# return nx,ny if there's land on fall. 
# return False if there's no land and fall into space  
def check_fall(x,y,gravity):
    if gravity:
        while True:
            x += 1 
            if x == N and mat[x][y]=='.':
                return False 
            elif mat[x][y] == '#':
                return (x-1,y) 
    else:
        while True:
            x -= 1 
            print(x,y)
            if x == 0 and mat[x][y]=='.':
                return False 
            elif mat[x][y] == '#':
                return (x+1,y)

def rescue(captain,doctor):
    while captain != doctor:
        cx,cy = captain
        dx,dy = doctor

        if cy < dy:
            fall = check_fall(cx,cy+1,gravity)
        elif cy > dy: 
            fall = check_fall(cx,cy-1,gravity)
        else:
            pass
        
        if not fall:
            gravity = not gravity
            fall = check_fall(cx,cy,gravity)
            if not fall:
                return -1
        captain = fall 
