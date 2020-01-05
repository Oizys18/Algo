# 주사위 굴리기

N, M, x, y, K = map(int,input().split())
nums = []
for _ in range(N):
    a,b = map(int,input().split())    
    nums.append((a,b))
orders = [*map(int,input().split())]