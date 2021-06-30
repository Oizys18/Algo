import sys
sys.stdin = open('BOJ17779.txt','r')
from pprint import pprint as pp
# 게리맨더링2
N = int(input())
mat =[[*map(int,input().split())] for _ in range(N)]

def isMap(x,y):
    return 0<=x<N and 0<=y<N
def fill(r,c,color):
    q = []
    q.append((r,c))
    check[r][c]=color
    while q:
        r,c = q.pop(0)
        for i in range(4):
            nr,nc = r+dx[i],c+dy[i]
            if not check[nr][nc]:
                q.append((nr,nc))
                check[nr][nc] = color
    pp(check)


dx=[0,0,-1,1]
dy=[-1,1,0,0]

# 기준점 x,y와 d1,d2가 정해지면 선거구가 결정됨 
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
                    one = 0
                    two = 0
                    three =0
                    four = 0
                    five = 0
                    for d in range(d1+1):
                        # five += mat[x+d][y-d]
                        # five += mat[x+d2+d][y+d2-d]
                        
                        check[x+d][y-d] = 5
                        check[x+d2+d][y+d2-d] = 5
                        if d == d1:
                            continue
                        # nr,nc = x+d+1,y-d
                        # while isMap(nr,nc) and check[nr][nc] != 5:
                        #     check[nr][nc] = 5 
                        #     nr += 1 

                    for dd in range(d2+1):
                        # five += mat[x+dd][y+dd]
                        # five += mat[x+d1+dd][y-d1+dd]
                        check[x+dd][y+dd] =5
                        check[x+d1+dd][y-d1+dd] = 5
                        if dd == d2:
                            continue
                        # nr,nc = x+dd+1,y+dd
                        # while isMap(nr,nc) and check[nr][nc] != 5:
                        #     check[nr][nc] = 5 
                        #     nr += 1 
                    

                    for r in range(N):
                        for c in range(N):
                            if not check[r][c]:
                                if 0 <= r <left[0] and 0<=c<=top[1]:
                                    check[r][c] = 1
                                    # one += mat[r][c]
                                elif 0<= r <= right[0] and top[1] < c <N:
                                    check[r][c] = 2
                                    # two += mat[r][c]
                                elif left[0]<= r <N and 0<= c < bottom[1]:
                                    check[r][c] = 3
                                    # three += mat[r][c]
                                elif right[0]< r < N and bottom[1]<= c < N : 
                                    check[r][c] = 4
                                    # four += mat[r][c]
                    pp(check)

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
                            elif check[a][b] == 5:
                                five += mat[a][b]

                    ans = min(max(one,two,three,four,five) - min(one,two,three,four,five), ans)
                    print(ans,'------------------')
print(ans)