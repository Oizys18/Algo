import sys
sys.stdin = open('input2.txt','r')


def binSearch(li, l, r, m, target):
    check = 0
    while True:
        if target < li[m]:
            if check == 1:
                return False
            r = m - 1
            m = (l+r)//2
            check = 1
        elif li[m] < target:
            if check == 2:
                return False
            l = m + 1
            m = (l+r)//2
            check = 2 
        elif li[m] == target:
            return True

# 양쪽 구간 번갈아 선택하는 경우만 센다. 
# 즉 왼쪽 < >오른쪽 
for T in range(int(input())):
    N, M = map(int,input().split())
    A = list(sorted(list(map(int,input().split()))))
    B = list(sorted(list(map(int,input().split()))))
    cnt = 0
    for b in B:
        if binSearch(A, 0, N-1, (N-1)//2, b):
            cnt += 1
    print("#{} {}".format(T+1,cnt))


