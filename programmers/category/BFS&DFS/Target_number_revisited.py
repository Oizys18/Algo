numbers = [1, 1, 1, 1, 1]
target = 3


# def solution(numbers, target):
#     import collections
#     answer = 0
#     stack = collections.deque([(0, 0)])
#     while stack:
#         _sum, _idx = stack.popleft()
#         if _idx == len(numbers):
#             if _sum == target:
#                 answer += 1
#         else:
#             stack.append((_sum+numbers[_idx], _idx+1))
#             stack.append((_sum-numbers[_idx], _idx+1))
#     return answer


# print(solution(numbers, target))

answer = 0
def solution(numbers, target):
    def recursive(_sum, idx):
        global answer
        if idx == len(numbers):
            if _sum == target:
                answer += 1
        else:
            recursive(_sum+numbers[idx], idx+1)
            recursive(_sum-numbers[idx], idx+1)
    recursive(0, 0)
    return answer


print(solution(numbers, target))
