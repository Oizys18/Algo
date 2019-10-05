import sys
sys.stdin = open('input2.txt','r')
for T in range(int(input())):
    d, m, m3, y = map(int,input().split())
    plan = list(map(int,input().split()))
    tempres = 0
    price_dm = [min(i*d,m) for i in plan]
    # temp = []
    # for i in range(10):
    #     if sum(price_dm[i:i+3]) > m3:
    #         temp.append(i) 
    # print(d,m,m3,y)
    # print(plan)
    # print(price_dm)
    # print(temp)

    # temptemp = 0
    # # for k in temp:
        

    visit = [0]*12
    for j in range(12):
        if visit[j]:    
            continue
        if j == 10 or j == 11:
            if j == 10:
                if sum(price_dm[j:j+2]) > m3:
                    if sum(visit[j:j+2]) == 0:
                        tempres += m3
                        visit[j:j+2] = [1,1]
            else:
                if price_dm[j] > m3:
                    if visit[j] == 0:
                        tempres += m3
                        visit[j] = 1
        if sum(price_dm[j:j+3]) > m3:
            if sum(visit[j:j+3]) == 0:
                tempres += m3
                visit[j:j+3] = [1,1,1]
            else:
                continue
        else:
            visit[j] = 1
            tempres += price_dm[j]
    print(f"#{T+1} {min(tempres,y)}")
