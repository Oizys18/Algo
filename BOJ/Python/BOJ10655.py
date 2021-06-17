#마라톤 
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ10655.txt', 'r')

N = int(input())
mat = [[*map(int,input().split())] for _ in range(N)]
shortest_length = 100000 * 4000
dp = [[0]*N for _ in range(N)]

for skip in range(0,2):
    pre = 0
    for now in range(1,N):
        print(pre,now+skip)
        if now+skip > N-1:
            break
        x1,y1 = mat[pre]
        x2,y2 = mat[now+skip]
        if not dp[pre][now+skip]:
            dp[pre][now+skip]= abs(x1-x2) + abs(y1-y2)
        pre = now 

# for skip in range(1,N-1):
#     length = 0
#     pre = 0 
#     for now in range(1,N):
#         if now == skip:
#             continue 
#         else:
#             print(pre,now)
#             x1,y1 = mat[pre]
#             x2,y2 = mat[now]
#             if not dp[pre][now]:
#                 dp[pre][now]= abs(x1-x2) + abs(y1-y2)
#             pre = now 
# pp(dp)

for skip in range(1,N-1):
    length = 0
    pre = 0
    for now in range(1,N):
        if now == skip:
            continue 
        else:
            print(pre,now)
            x1,y1 = mat[pre]
            x2,y2 = mat[now]
            length += abs(x1-x2) + abs(y1-y2)
            pre = now 
    shortest_length = min(length, shortest_length)
print(shortest_length)