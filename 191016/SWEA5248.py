import sys
sys.stdin = open('input7.txt','r')

for T in range(int(input())):
    N, M = map(int,input().split())
    checkList = list(map(int,input().split()))
    zo = {}
    for i in range(0,len(checkList),2):
        if checkList[i] not in zo.keys():
            zo[checkList[i]] = []
        