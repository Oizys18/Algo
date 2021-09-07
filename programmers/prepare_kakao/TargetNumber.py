answer = 0
def solution(numbers, target):
    global answer
    N = len(numbers)
    def solve(value,k):
        global answer
        if k == N:
            if value == target:
                answer += 1       
            return 
        else:
            solve(value + numbers[k], k+1)
            solve(value - numbers[k], k+1)   
    solve(0,0)   
    return answer



"""
새로 푼 풀이, 이전 풀이 안보고 풀었는데 아예 똑같다. 
단지 재귀함수의 결과값을 global 변수를 사용하지 않고 list를 사용해서 값을 저장했다. 
"""
def solution(numbers, target):
    answer = [0]
    N = len(numbers)
    def recur(total,k):
        if k == N:
            if total == target:
                answer[0] += 1
            return 
        else:
            recur(total+numbers[k], k+1)
            recur(total-numbers[k], k+1)
    recur(0,0)
    return answer[0]