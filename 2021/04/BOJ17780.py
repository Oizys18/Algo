# 새로운 게임
import sys
sys.stdin = open('BOJ17780.txt','r')
from pprint import pprint as pp 


# 다음 칸 정보 확인 
def check_next (nx,ny):
    return 0 <= nx < N and 0 <= ny <N and info_mat[nx][ny]!=2

#방향전환
def change_direction(direction):
    if direction%2:return direction+1
    return direction-1

# 방향, →, ←, ↑, ↓
mv = {
    1: (0,1),
    2: (0,-1),
    3: (-1,0),
    4: (1,0)
}

N,K = map(int,input().split())
info_mat = [list(map(int,input().split())) for _ in range(N)]
mat = [[[] for _ in range(N)] for _ in range(N)]
data = []

for k in range(K):
    x,y,direction = map(int,input().split())
    mat[x-1][y-1].append(k)
    data.append([k,x-1,y-1,direction])

def solve():
    for turn in range(1000):
        for k,x,y,d in data:
            if mat[x][y][0] != k: continue
            nx, ny = x+mv[d][0], y+mv[d][1]

            if not check_next(nx,ny):
                # blue || out of range : 방향전환
                d = change_direction(d)
                data[k][3] = d
                nx, ny = x+mv[d][0], y+mv[d][1] 

                if not check_next(nx,ny):
                    continue
            if info_mat[nx][ny]==1:
                mat[x][y].reverse()

            mat[nx][ny] += mat[x][y]
            mat[x][y] = [] 

            for nk in mat[nx][ny]:
                data[nk][1] = nx
                data[nk][2] = ny
            if len(mat[nx][ny])>=4:
                return turn +1
    return -1

print(solve())

"""
또 시간 많이 걸렸다.. 시뮬레이션에서 자꾸 실수가 많이 나오는듯 
처음부터 조건별로 어떻게 코드 짤 지 생각해보고 짜는 습관을 들여야겠음 

1.direction 방향 수정할 때 모듈로 사용하는 부분 
2. 다음 칸 정보 확인하는 부분에서 1. 맵 안에 있고 2. 파란색이 아니다! 일 때만 True 반환하는 걸로 말 순서 바꾸는 부분을 나누고 
    46-47에서 한 번 더 체크 후 2번 연속으로 파랑/맵밖이라면 continue로 때려버리고, 이후에 48부터 한 칸 진행해버리는 방법
3. 빈 어레이를 만들어서 그 위에서 실제로 말들을 옮겨가며 체크하는 방법 

이 3가지를 중점적으로 기억하자. 

처음 나는 
1-> if/else로 각각 switch 처럼 방향 전환함 
2-> white, red, blue, False(맵 아웃) 으로 나누어 각각 조건별로 말을 이동하려다보니 매우 헷갈렸다. 
3-> 말의 위치, 좌표 별 현재 말, 말의 방향, 말 스택 의 4가지 딕셔너리로 하려고 했더니 너어어어어무 헷갈렸다. 
    이전에 메모리 초과/ 시간초과로 한 번 데였더니 딕셔너리를 불필요하게 사용하려고 했나봄 ㅠ 


"""