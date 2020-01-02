import sys
sys.stdin = open('input5.txt','r')

from itertools import combinations
N = int(input())
week = {}
weeks = {}
for i in range(1,N+1):
    week[i] = tuple(map(int,input().split()))
    weeks[i] = []
for j in range(1,N+1):
    if j + week[j][0] - 1 > N:
        continue
    else:
        weeks[j] = [i for i in range(j + week[j][0],N+1) if i + week[i][0] - 1 <= N]


def DFS(node):
    if len(weeks[node]) == 0:
        workday.append(visit.copy())
    else:
        for i in weeks[node]:
            visit.append(i)
            DFS(i)
            visit.pop()

workday = []
for i in weeks.keys():
    # print(i)
    if len(weeks[i]) == 0 and week[i][0] + i -1 > N:
        # print('1')
        continue
    visit = [i]
    (DFS(i))
# print(workday)
result = 0

for day in workday:
    money = 0
    for v in day:
        money += week[v][1]
    if result < money:
        result = money
    
print(result)