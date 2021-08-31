numbers = '011'
from itertools import permutations
import math 
def check_sosu(n):
    if n == 1 or n==0:
        return False
    for i in range(2, int(math.floor(math.sqrt(n)))+1):
        if n%i==0:
            return False
    return True 

def solution(numbers):
    answer = 0
    ans_set = set()
    for i in range(1,len(numbers)+1):
        for x in set([int(''.join(x)) for x in permutations(numbers,i)]):
            if check_sosu(x):
                ans_set.add(x)
    answer = len(ans_set)
    return answer 

print(solution(numbers))