#4880
import sys
sys.stdin = open('input5.txt','r')

for T in range(int(input())):
    N = int(input())
    cards = list(map(int,input().split()))
    # print(cards)
    stack = []
    stack.append(cards)

    while stack:
        card = stack.pop()
        print(card)
        if len(card) != 1:
            stack.append(cards[0:(0+len(cards))//2])
            stack.append(cards[(0+len(cards))//2:])
            print(stack)
