# SWEA 1244

import sys
sys.stdin = open('input.txt','r')


# def shuffle(li):
#     end = li[-1]
#     visit = 
#     # find change max
#     max(li)
#     for idx, num in enumerate(li):
#         if end > num:
#             li[idx], li[-1] = li[-1], li[idx] 
#             break
#         elif idx == len(li) - 2:
#             li[idx], li[-1] = li[-1], li[idx]
#             break

for T in range(int(input())):
    cards, chance = input().split()
    chance = int(chance) 

    
    total = []

    # while chance:
    #     shuffle(cards)
    #     chance -= 1
    print(cards, chance)
    # print(deck)