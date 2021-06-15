import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ1027.txt', 'r')

N = int(input())
buildings = [*map(int,input().split())]


def solve(N,buildings):
    def check(front,mid,back):
        if buildings[front] == buildings[mid] or buildings[mid] == buildings[back]:
            return False
        elif min(buildings[front],buildings[mid],buildings[back]) == buildings[mid]:
            return True
        elif buildings[front] < buildings[back]:
            if ((buildings[back]-buildings[front])/(back-front))*(mid-front) + buildings[front] > buildings[mid]:
                return True
        elif buildings[front] > buildings[back]:
            if ((buildings[front]-buildings[back])/(back-front))*(back-mid) + buildings[back] > buildings[mid]:
                return True
        elif max(buildings[front],buildings[mid],buildings[back]) == buildings[mid]:
            return False
        elif buildings[front] == buildings[back]:
            return True  
    answer = 0
    for i in range(N):
        visible = 0
        top = 0

        topIdx = i
        for j in range(i+1,N):
            if top == 0:
                visible+=1
            elif check(i,topIdx,j):
                visible += 1
            if buildings[j] > top:
                top = buildings[j]
                topIdx = j

        top = 0
        topIdx = i
        for j in range(i-1,-1,-1):
            if top == 0:
                visible+=1
            elif check(j,topIdx,i):
                visible += 1

            if buildings[j] > top:
                top = buildings[j]
                topIdx = j

        answer = max(answer,visible)
    return answer 
#  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
# [1, 5, 3, 2, 6, 3, 2, 6, 4, 2, 5, 7, 3, 1, 5]

print(solve(N,buildings))