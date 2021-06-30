import sys
sys.stdin = open('BOJ17779.txt','r')
from pprint import pprint as pp
# 게리맨더링2
N = int(input())
mat =[[*map(int,input().split())] for _ in range(N)]
def isMap(x,y):
    return 0<=x<N and 0<=y<N
total = sum([*map(sum,mat)])
ans = 200000
for x in range(N-1):
    for y in range(1,N-1):
        for d1 in range(1,y+1):
            for d2 in range(1,N-x-d1+1):
                top =(x,y)
                left = (x+d1,y-d1)
                bottom = (x+d1+d2,y-d1+d2)
                right = (x+d2,y+d2)

                fives = set()
                if isMap(bottom[0],bottom[1]) and isMap(right[0],right[1]):
                    for d in range(d1+1):
                        fives.add((x+d,y-d))
                        fives.add((x+d2+d,y-d+d2))
                    for dd in range(d2+1):
                        fives.add((x+dd,y+dd))
                        fives.add((x+d1+dd,y-d1+dd))

                    t1 = 0
                    for r in range(left[0]):
                        for c in range(top[1]+1):
                            if (r,c) in fives:break
                            t1 += mat[r][c]
                    t2 = 0
                    for r in range(right[0]+1):
                        for c in range(N-1,top[1],-1):
                            if (r,c) in fives:break
                            t2 += mat[r][c]
                    t3 = 0
                    for r in range(left[0],N):
                        for c in range(bottom[1]):
                            if (r,c) in fives:break
                            t3 += mat[r][c]
                    t4 = 0
                    for r in range(right[0]+1,N):
                        for c in range(N-1,bottom[1]-1,-1):
                            if (r,c) in fives:break
                            t4 += mat[r][c]

                    t5 = total - (t1+t2+t3+t4)
                    ans = min(ans,max(t1,t2,t3,t4,t5)-min(t1,t2,t3,t4,t5))
print(ans)

"""
첫번째 풀이로 정답이었지만 시간이 너무 오래걸려서, 
다시 한번 다른 풀이로 풀었다. 
일단 처음 모든 값을 더한 total을 구하는 방식으로 5번째 구역을 굳이 다시 계산할 필요없도록 했고, 
다음으로 5번 영역을 set으로 계산해서 매번 check[][]를 만들 필요가 없도록 했으며 
마지막으로 각 영역을 이중for문 + break로 계산했다. 

물론 그래도 dfs 한 것 보다는 속도가 느리지만.. 어쩔 수 없지..
"""


"""
# d1,d2 정해서 5의 경계를 그린다음 
# 좌측상단, 좌측 하단, 우측상단, 우측하단에 각각 bfs돌리고
# 각 영역 계산해줬음  
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
    total = 0
    q = []
    q.append((r,c))
    check[r][c]=color
    total += mat[r][c]
    while q:
        r,c = q.pop(0)
        for i in range(4):
            nr,nc = r+dx[i],c+dy[i]
            if func(nr,nc,dr1,dr2):
                q.append((nr,nc))
                check[nr][nc] = color
                total += mat[nr][nc]
    return total

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

                    one = fill(0,0,1,isOne,top,left)
                    two =fill(0,N-1,2,isTwo,top,right)
                    three =fill(N-1,0,3,isThree,left,bottom)
                    four = fill(N-1,N-1,4,isFour,right,bottom)
                    five = 0
                    for a in range(N):
                        for b in range(N):
                            if check[a][b] == 5 or not check[a][b]:
                                five += mat[a][b]

                    ans = min(max(one,two,three,four,five) - min(one,two,three,four,five), ans)
print(ans)
"""