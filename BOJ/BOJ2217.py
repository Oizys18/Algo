# 로프
import collections
N = int(input())
li = collections.deque(sorted([int(input()) for _ in range(N)]))
res = 0
while li:
    k = len(li)
    w = li.popleft()
    if res < w*k:
        res = w*k
print(res)
    