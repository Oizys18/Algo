N = int(input())
weekdays = []
for _ in range(N):
    a, b = map(int,input().split())
    weekdays.append((a,b))

res = 0

def solve(day, profit):
    global res
    if day >= N:
        if profit > res:
            res = profit
        return 
    else:
        # 상담 O
        if day + weekdays[day][0] <= N:
            solve(day+weekdays[day][0], profit+weekdays[day][1])
        # 상담 X
        if day + 1 <= N+1:
            solve(day+1, profit)
solve(0,0) 
print(res)