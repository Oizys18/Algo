import sys
sys.stdin = open('BOJ17779.txt','r')
from pprint import pprint as pp
# 게리맨더링2
N = int(input())
mat =[[*map(int,input().split())] for _ in range(N)]
pp(mat)
# 기준점 x,y와 d1,d2가 정해지면 선거구가 결정됨 
#  0 < x <=N and 0 < y <= N 
# 1 <= d1+d2 < N-x 
# 1 ≤ x < x+d1+d2 ≤ N  
#  1 ≤ y-d1 < y < y+d2 ≤ N

# 0 < d1 <= y-1
# 0 < d2 <= N-y

for x in range(N):
    for y in range(1,N-1):
        for d1 in range(1,y):
            for d2 in range(1,N-y-1):
                print(x,y,d1,d2)




# 기준점 x,y 
def solve(x,y):
    # return 넓이차 
    pass