import sys 
sys.stdin = open('BOJ1036.txt','r')
from pprint import pprint as pp 

from collections import defaultdict

N = int(input())
nums = [input() for _ in range(N)]
K = int(input())
tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nd = defaultdict(int)
for num in nums:
    n = len(num)
    for i,v in enumerate(num):
        nd[v] +=int(('Z'+'0'*(n-i-1)),36) - int((v+'0'*(n-i-1)),36)
turnK = []

for k in reversed(sorted(nd.keys(),key=lambda x:nd[x])):
    if K and k !='Z':
        turnK.append(k)
        K-=1
    else:
        break
for tk in turnK:
    nums = [num.replace(tk,'Z') for num in nums]
answer = 0 
for num in nums:
    answer += int(num,36)

def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
print(convert(answer,36))