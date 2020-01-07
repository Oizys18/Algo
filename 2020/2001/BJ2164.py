# 카드2
import collections
N = int(input())
N_li = collections.deque([i for i in range(1,N+1)])
res = 0
while True:
    if len(N_li) == 1:
       res = N_li.pop()
       break 
    N_li.popleft()
    second = N_li.popleft()
    N_li.append(second)

print(res)