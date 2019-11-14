from pprint import pprint as pp
import sys
sys.stdin=open('4012.txt','r')


# import itertools
# int(input())
# for T in range(10):
#     N = int(input())
#     mat = [list(map(int,input().split())) for _ in range(N)]
#     nums = {i for i in range(N)}
#     result = 10000
#     for i in itertools.combinations(nums,N//2):


#         temp1 = 0
#         for j in itertools.combinations(i,2):
#             a,b = j
#             temp1 += mat[a][b] + mat[b][a]
        
        
#         li2 = nums - set(i)
#         temp2 = 0
#         for l in itertools.combinations(li2,2):
#             a,b = l
#             temp2 += mat[a][b] + mat[b][a]
#         res = abs(temp1-temp2)
#         if res <= result:
#             result = res
#     print(f"#{T+1} {result}")






def comb(k, s):
    if k == R:
        print(temp)
        # for i in temp.copy():
            
        # temp2 = set(nums) - set(temp.copy())
    else:               # N - R + 1 + k   : N 뽑을 곳의 갯수 R 뽑을 갯수, k Depth  
        for i in range(N):
            temp[k] = nums[i]
            comb(k + 1, i + 1)



int(input())
for T in range(3):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    nums = [i for i in range(N)]
    result = 10000
    temp = [0]*(N//2)
    R = (N//2)
    comb(0,0)
    
