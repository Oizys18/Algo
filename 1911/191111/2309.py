# 2309.py 일곱난쟁이
import itertools
dwarves = []
realdwarves = []
for i in range(9):
    dwarves.append(int(input()))
for j in itertools.combinations(dwarves,7):
    if sum(j) == 100:
        realdwarves = list(sorted(j))
        break
for k in realdwarves:
    print(k)
