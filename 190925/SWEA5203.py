#SWEA5203


import sys
sys.stdin = open('input5.txt','r')


def BG(li):
    print(li)
    cnt = 0
    for i in li:
        if i == 3:
            return True
        elif i:
            cnt +=1 
            if cnt == 3:
                return True
        elif i == 0:
            cnt = 0
    return False
    

for T in range(int(input())):
    line = list(map(int,input().split()))
    p1 = [0]*10
    p2 = [0]*10
    res = 0

    for i in range(len(line)):
        if i % 2 == 0:
            p1[line[i]] += 1
        else:
            p2[line[i]] += 1
        if BG(p1):
            res = 1
            break
        elif BG(p2):
            res = 2
            break
    print("#{} {}".format(T+1,res))
