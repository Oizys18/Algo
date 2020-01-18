# 극장좌석

N = int(input())
seats = [0]*(N+1)
M = int(input())
for _ in range(M):
    seats[int(input())] = 1
print(seats)

def solve():
    