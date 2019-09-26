import sys
sys.stdin = open('input2.txt','r')
cnt = 0
def divide(li):
    N = len(li)
    if len(li) == 1:
        return li
    # l = li[0:N//2]
    # r = li[N//2:N]
    l = divide(li[0:N//2])
    r = divide(li[N//2:N])
    return merge(l,r)

def merge(left,right):
    global cnt
    result = []
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) > 0 or len(right) > 0 :
        if len(left) > 0 and len(right)>0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left)>0:
            result.append(left.pop(0))
        elif len(right)>0:
            result.append(right.pop(0))
    return result

for T in range(int(input())):
    N = int(input())
    nums = list(map(int,input().split()))
    cnt = 0
    print("#{} {} {}".format(T+1,divide(nums)[N//2],cnt))



