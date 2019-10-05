import itertools

arr = [1,2,3,4,5]
for j in range(1,5+1):
    for i in itertools.combinations(arr,j):
        if sum(i) > 10:
            continue
        print(list(i))