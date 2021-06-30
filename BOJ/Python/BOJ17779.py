import sys
sys.stdin = open('BOJ17779.txt','r')
from pprint import pprint as pp
# 게리맨더링2
N = int(input())
mat =[[*map(int,input().split())] for _ in range(N)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def isMap(x,y):
    return 0<=x<N and 0<=y<N
def isOne(x,y,top,left):
    return 0 <= x <left[0] and 0<=y<=top[1] and check[x][y]!=5 and not check[x][y] 
def isTwo(x,y,top,right):
    return 0<= x <= right[0] and top[1] < y <N and check[x][y]!=5 and not check[x][y]
def isThree(x,y,left,bottom):
    return left[0]<= x <N and 0<= y < bottom[1] and check[x][y]!=5 and not check[x][y]
def isFour(x,y,right,bottom):
    return right[0]< x < N and bottom[1]<= y < N and check[x][y]!=5 and not check[x][y]

def fill(r,c,color,func,dr1,dr2):
    q = []
    q.append((r,c))
    check[r][c]=color
    while q:
        r,c = q.pop(0)
        for i in range(4):
            nr,nc = r+dx[i],c+dy[i]
            if func(nr,nc,dr1,dr2):
                q.append((nr,nc))
                check[nr][nc] = color

ans = 2000
for x in range(N-1):
    for y in range(1,N-1):
        for d1 in range(1,y+1):
            for d2 in range(1,N-x-d1+1):
                check = [[0]*N for _ in range(N)]
                top =(x,y)
                left = (x+d1,y-d1)
                bottom = (x+d1+d2,y-d1+d2)
                right = (x+d2,y+d2)

                if isMap(bottom[0],bottom[1]) and isMap(right[0],right[1]):
                    for d in range(d1+1):
                        check[x+d][y-d] = 5
                        check[x+d2+d][y+d2-d] = 5
                    for dd in range(d2+1):
                        check[x+dd][y+dd] =5
                        check[x+d1+dd][y-d1+dd] = 5

                    fill(0,0,1,isOne,top,left)
                    fill(0,N-1,2,isTwo,top,right)
                    fill(N-1,0,3,isThree,left,bottom)
                    fill(N-1,N-1,4,isFour,right,bottom)


                    one = 0
                    two = 0
                    three = 0
                    four = 0
                    five = 0

                    for a in range(N):
                        for b in range(N):
                            if check[a][b] == 1:
                                one += mat[a][b]
                            elif check[a][b] == 2:
                                two += mat[a][b]
                            elif check[a][b] == 3:
                                three += mat[a][b]
                            elif check[a][b] == 4:
                                four += mat[a][b]
                            elif check[a][b] == 5 or not check[a][b]:
                                five += mat[a][b]

                    ans = min(max(one,two,three,four,five) - min(one,two,three,four,five), ans)
print(ans)