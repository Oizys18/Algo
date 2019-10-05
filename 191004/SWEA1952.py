import sys
sys.stdin = open('input2.txt','r')

def MorD(day):
    if day*d > m:
        return m
    else:
        return day * d

for T in range(int(input())):
    d, m, m3, y = map(int,input().split())
    plan = list(map(int,input().split()))
    expense = y
    tempres = 0
    # price_dm = [min(i*d,m) for i in plan]
    # print(day_month)
    
    while sum(plan) > 0:
        print(plan)
        temp = []
        temp3 = []
        flag = 0
        for i in range(12):
            if i == 10 or i == 11:
                temp = plan[i:]
            else:
                temp = plan[i:i+3]
            if sum(temp) >  sum(temp3):
                ri = i
                temp3 = temp 
        tdm = 0
        for t in temp3:
            tdm += MorD(t)
        
        if m3 < tdm and m3 < tdm:
            tempres += m3
        else:
            tempres += tdm
        if ri == 10:
            plan[10] = 0
            plan[11] = 0
        elif ri == 11:
            plan[11] = 0
        else:
            plan[ri:ri+3] = [0,0,0]
        flag = 1
        continue
    if tempres < expense:
        expense = tempres
    print(expense)