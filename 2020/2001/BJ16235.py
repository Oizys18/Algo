# 나무 사재기
from pprint import pprint as pp 
N, M, K = map(int, input().split())
mat = [[5]*N for _ in range(N)]
foo = [[*map(int, input().split())] for _ in range(N)]
start_tree = [[*map(int, input().split())] for _ in range(M)]
dxdy = [(-1,-1), (-1, 0), (-1,1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# pp(mat)
# pp(foo)
# pp(tree)

def isMap(x,y):
    if 0 <= x < N and 0 <= y < M:
        return True
    else:
        return False

def work():
    pass

