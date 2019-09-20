import sys
sys.stdin = open('input.txt', 'r')
from pprint import pprint as pp 


# def sort(line):
#     return sorted(line)

# def stack(start):
#     stack = [range(N)]
#     visit = [0]*N
#     stack.append(start)
#     while stack:
#         node = stack.pop()

def perm_r_2(k):
    if k == N:
        print(arr[0], arr[1], arr[2])
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm_r_2(k + 1)
            arr[k], arr[i] = arr[i], arr[k]




for T in range(int(input())):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    mat2 = [list(i) for i in zip(*mat)]
    for i in mat:
        arr = i
        for j in arr:
            perm_r_2(j)
    