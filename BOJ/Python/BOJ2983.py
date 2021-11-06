from pprint import pprint as pp
import sys
sys.stdin = open('BOJ2983.txt', 'r')

N, K = map(int, sys.stdin.readline().split())
directions = sys.stdin.readline().strip()
leaves = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
pp(leaves)


mnleaf = min(leaves)
mxleaf = max(leaves)
leaf = leaves.pop(0)

dr = {
    'A': lambda x: (x[0]+1, x[1]+1),
    'B': lambda x: (x[0]+1, x[1]-1),
    'C': lambda x: (x[0]-1, x[1]+1),
    'D': lambda x: (x[0]-1, x[1]-1),
}


def jump(leaf, direction):
    temp = leaf
    flag = 0
    while 0 <= temp[0] <= 1000000000 and 0 <= temp[1] <= 1000000000:
        temp = dr[direction](temp)
        if temp in leaves:
            flag = 1
            break
        if temp[0] < mnleaf[0] or temp[0] > mxleaf[0]:
            break
    if flag:
        leaves.remove(temp)
        return temp
    else:
        return leaf


for direction in directions:
    leaf = jump(leaf, direction)
print(*leaf)


""" 
jump 중 효율성을 높여야한다. 
A의 경우 x,y 좌표의 차이가 그대로 유지되면서 값이 증가한다. 
B의 경우 x+P y-P니까 두 값의 차이가 2P가 된다. (2P, 2P+2, ... N(P+1))
C의 경우 B와 유사하다 
D의 경우 A와 유사한데 값이 감소한다. 

점프유형  두 값의 차 (x-y) 
    A       0
    B       2P, 2P+2, ..., 2P+N
    C       -2P, -2P-2, ..., -2P-N
    D       0

jump 함수에서 방향값과 현재 좌표를 받아서 
남은 leaves 중 현재 점프 유형에서 두 값의 차가 위와같은 경우를 제일 먼저 만족하는 좌표를 뱉어야한다. 
점프수는 100000, 좌표는 (0,0)에서 (1,000,000,000,1,000,000,000)까지. 
heap으로 해야할 것 같다. 

시간제한 1초,메모리 128mb제한 
"""
