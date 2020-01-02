import sys
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    N = int(input())
    nums = list(map(int,input().split()))
    print(sorted(nums)[N//2])
