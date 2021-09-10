def solution(n, times):
    answer = 0
    times.sort()
    N = len(times)
    calc = [list(map(lambda x:x*i, times)) for i in range(1,n//N+3)]
    check = [element for array in calc for element in array]
    return sorted(check)[n-1]
    
"""
첫 풀이, 시간초과 & 오답 
이후 heap을 사용해서 풀어보려고 했지만 얄짤없었다. 

결국 해결방법 확인해보자 이진탐색 문제였다...! 

생각해보니 최솟값 (times[0]) 최댓값 (n*times[0])이 존재하고, 목표값이 있으니까 이진탐색에 맞다. 
문제는 condition인데, 아래 코드 중 condition에서 보면, 
value(mid값)을 time의 값으로 각각 나눠보고 그 몫을 모두 더하면 각 값이 해당 value에서 처리할 수 있는 고객수가 나온다..!
생각해보면 간단함 

그래서 이전에 leetcode에서 가져온 이진탐색 코드로 돌려보니 정답이었다 ㅠ 
"""



def solution(n, times):
    times.sort()
    def binary_search(array) -> int:
        def condition(value) -> bool:
            return sum(value//time for time in times) >= n
        
        left, right = array[0], array[0]*n 
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    return binary_search(times)
    
    
    
