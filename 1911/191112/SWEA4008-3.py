# SWEA 4008 계산기 retry
import sys
sys.stdin = open('4008.txt','r')
int(input())
cnt = 0
def solve(k, res):
    global minRes
    global maxRes
    global cnt
    cnt += 1
    
    if k == N:
        if res <= minRes:
            minRes = res
        if res >= maxRes:
            maxRes = res
        return 

    else:
        if operator[0]:
            operator[0] -= 1
            solve(k+1, res + nums[k])
            operator[0] += 1

        if operator[1]:
            operator[1] -= 1
            solve(k+1, res - nums[k])
            operator[1] += 1
        
        if operator[2]:
            operator[2] -= 1    
            solve(k+1, res * nums[k])
            operator[2] += 1

        if operator[3]:
            operator[3] -= 1
            solve(k+1, int(res / nums[k]))
            operator[3] += 1
        

for T in range(1):
    N = int(input())
    operator = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    minRes = 100000000
    maxRes = -100000000 
    
    
    solve(1, nums[0])
    print(maxRes-minRes)    