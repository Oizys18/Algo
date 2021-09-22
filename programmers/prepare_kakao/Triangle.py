from pprint import pprint as pp
def solution(triangle):
    answer = 0
    N = len(triangle)
    dp = [0]*N
    pp(triangle)
    pp(dp)
    
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(triangle))