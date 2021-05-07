import sys
sys.stdin=open('BOJ2675.txt','r')

T = int(input())

for _ in range(T):
    R,S = input().split()
    R = int(R)
    ans = ''    
    for w in S:
        ans += w*R
    print(ans)