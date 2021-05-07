import sys
sys.stdin=open('BOJ2577.txt','r')
num = 1
for _ in range(3):
    num *= int(input())

num = str(num)

for k in range(10):
    print(num.count(str(k)))