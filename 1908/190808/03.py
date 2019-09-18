#SWEA 4839 Binary Search!

# Binary Search Function as binS 
def binS(total,target):
    cnt = 0
    l = 1
    r = total
    while True:
        c = int((l+r)/2)
        cnt += 1
        if c == target:
            return cnt
        elif target > c:
            l = c
        else:
            r = c

for T in range(int(input())):
    total, tarA, tarB = map(int,input().split())
    cntA = binS(total,tarA)
    cntB = binS(total,tarB)
    if cntA < cntB:
        win = 'A'
    elif cntB < cntA:
        win = 'B'
    elif cntA == cntB:
        win = 0

    """
    #default 값 부여 후 비교하는 방법 / 조건문 한 번 적게 사용!  
    win = 0 
    if cntA < cntB:
        win = 'A'
    elif cntB < cntA:
        win = 'B' 
    """
    print("#{0} {1}".format(T+1, win))

