def solution(array, commands):
    answer = []
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

# 더 줄여봤다.


def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]