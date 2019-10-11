import sys
sys.stdin= open('input3.txt','r')

# def heap(node):
#     if tree[-1] < node:
        
#     else:


for T in range(int(input())):
    N = int(input())
    line = [0] + list(map(int,input().split()))
    heap = [0]*(N+1)
    # for i in range(1,N+1):
    #     line[i]
