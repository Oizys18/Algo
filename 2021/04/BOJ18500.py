import sys
sys.stdin = open('BOJ18500.txt','r')
from pprint import pprint as pp
import time
start = time.time()
from collections import deque

def isMineral(x,y):
    if 0 <= x < R and 0 <= y < C and mat[x][y]!=0:return True

def isMap(x,y):
    if 0 <= x < R and 0 <= y < C: return True 

def getCluster():
    cluster = 0
    floating = 0
    visit = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if mat[x][y] and not visit[x][y]:
                isLanded = 0
                cluster += 1        
                queue = deque()
                queue.appendleft((x,y))
                visit[x][y] = 1
                while queue:
                    x,y = queue.popleft()
                    mat[x][y] = cluster
                    if x == R-1:isLanded = 1
                    for i in range(4):
                        nx,ny = x+dx[i], y+dy[i]
                        if isMineral(nx,ny) and not visit[nx][ny]:
                            queue.appendleft((nx,ny))
                            visit[nx][ny] = 1
                if not isLanded:
                    floating = cluster
    return floating

def throw(stone,i):
    x = R - stone
    if i%2: # 1,3,5,7 ... <-
        for y in range(C-1,-1,-1):
            if mat[x][y]:
                mat[x][y] = 0
                return 
    else: # 0,2,4,6 ... ->  
        for y in range(C):
            if mat[x][y]:
                mat[x][y] = 0
                return 


def drop(floating):
    temp = []
    for x in range(R):
        for y in range(C):
            if mat[x][y] == floating:
                temp.append((x,y))
    temp.sort(reverse=True)
    far = 2
    flag = 0
    while not flag:
        for x,y in temp:
            if (x+far,y) in temp:
                continue
            if not isMap(x+far,y) or (isMineral(x+far,y)):
                flag = 1
        if not flag:
            far += 1

    for x,y in temp:
        if mat[x+far-1][y] == mat[x][y]:
            continue
        mat[x+far-1][y],mat[x][y] = mat[x][y],0

R,C = map(int,input().split())
mat = [[0 if i=='.' else 1 for i in input()] for _ in range(R)]

N = int(input())
stones = list(map(int,input().split()))

# direction
dx = [-1,1,0,0]
dy = [0,0,1,-1]

for i in range(len(stones)):
    throw(stones[i],i)
    floating = getCluster()
    if floating:drop(floating)

for x in range(R):
    print(''.join(['x' if mat[x][y] else '.' for y in range(C)]))


"""
시간초과 때문에 고생했다. 
import time 
start = time.time()
print('time:',time.time()-start)
사용해서 시간을 재봤다. 

확인해보니 
1. while을 사용해서 오래 걸릴거라고 예상했던 돌을 떨어뜨리는 구간에서 생각보다 빨리 처리됐음. 문제원인 아니었다. 
2. cluster(집단) 구하는 부분에서 매번 0.02초 씩 걸렸고, 100번 실행만 되도 2초니까 제한시간인 1초를 훌쩍 뛰어넘는 속도였다. 문제원인이었음 
    - 자세히 확인해보니, 처음 구현할 때 clustering 함수에서 아예 다음에 떨어질 돌을 return 한다면 처리가 효율적일 거라고 생각해서 append 사용했는데, 오히려 이게 문제였다.
    - 그냥 어떤 cluster가 현재 공중에 떠있는지만 체크해서 return 한 후, drop()함수에서 행열을 한번 순환하면서 해당 클러스터의 좌표만을 뽑아내 새로운 배열을 생성하는게 속도가 빨랐다. 

결론 
- append()함부로 쓰지 말자. 특히 iteration 중일 때는 최소한으로 쓰고, 아예 배열 한번 더 도는게 빠를 수도 있다.  
- 속도저하의 원인은 배열을 도는 것보다 배열 돌 때 매번 특정 라인을 실행시킬 때 더 문제가 된다. 
"""