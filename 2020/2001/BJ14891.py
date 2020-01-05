# 톱니바퀴

a = int(input())
b = int(input())
c = int(input())
d = int(input())
K = int(input())
rot = {}
for _ in range(K):
    idx, direc = map(int,input().split())
    rot[idx] = direc