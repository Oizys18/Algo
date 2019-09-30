import sys
sys.stdin = open('input2.txt','r')
cnt = 0

# 실제 소팅하지 않고 그냥 가장 큰 값만 보면 성능 올라갈 것 

def divide(li):
    N = len(li)
    if N == 1:
        return li
    return merge(divide(li[0:N//2]),divide(li[N//2:N]))

def merge(left, right):
    global cnt
    # result = []
    result = sorted(left + right)
    if left[-1] > right[-1]:
        cnt += 1
    return result

for T in range(int(input())):
    N = int(input())
    nums = list(map(int,input().split()))
    cnt = 0
    print("#{} {} {}".format(T+1,divide(nums)[N//2],cnt))
