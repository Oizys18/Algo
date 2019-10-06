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
    price_dm = [min(i*d,m) for i in plan]
    print(plan)
    print(price_dm)

    

    while sum(plan) > 0:
        t4 = []
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
                t4.append(temp)
        print(t4)
        temp3 = max(t4)
        print(temp3)
        tdm = 0
        for t in temp3:
            tdm += MorD(t)
        print(tdm)
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
        print(plan)
        continue
    if tempres < expense:
        expense = tempres
    print(expense)
"""
10
10 40 100 300
0 0 2 9 1 5 0 0 0 0 0 0
10 100 50 300
0 0 0 0 0 0 0 0 6 2 7 8
10 70 180 400
6 9 7 7 7 5 5 0 0 0 0 0
10 70 200 550
0 0 0 0 8 9 6 9 6 9 8 6
10 80 200 550
0 8 9 15 1 13 2 4 9 0 0 0
10 130 360 1200
0 0 0 15 14 11 15 13 12 15 10 15
10 180 520 1900
0 18 16 16 19 19 18 18 15 16 17 16
10 100 200 1060
12 9 11 13 11 8 6 12 8 7 15 6
10 170 500 1980
19 18 18 17 15 19 19 16 19 15 17 18
10 200 580 2320
12 28 24 24 29 25 23 26 26 28 27 22
"""