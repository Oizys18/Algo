# 1,2,3 더하기



for T in range(int(input())):
    n = int(input())
    res = 0
    
    temp = []
    def solve(n):
        global res
        if n == 0:
            res += 1
            return
        else:
            if n >= 3:
                temp.append(3)
                solve(n-3)
                temp.pop()
            if n >= 2:
                temp.append(2)
                solve(n-2)
                temp.pop()
            if n >= 1:
                temp.append(1)
                solve(n-1)
                temp.pop()
    solve(n)
    print(res)