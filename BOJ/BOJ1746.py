import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ1746.txt', 'r')

N,M = map(int,input().split())
unheard = set(input() for _ in range(N))
unseen = set(input() for _ in range(M))
unseenNheard = unseen.intersection(unheard)
print(len(unseenNheard))
unseenNheard = list(unseenNheard)
unseenNheard.sort()
for person in unseenNheard:
    print(person)
