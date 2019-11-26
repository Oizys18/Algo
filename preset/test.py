# import itertools

# arr = [1,2,3,4,5]
# for j in range(1,5+1):
#     for i in itertools.combinations(arr,j):
#         if sum(i) > 10:
#             continue
#         print(list(i))


# for i in range(20):
    
#     print(i)
#     if i > 5:
#         print(i%5)
import random
seen = [j for j in range(0,18)]
picked = random.sample([i for i in range(0,20) if i not in seen],3)
print(picked)