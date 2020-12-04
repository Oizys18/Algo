def solution(number, k):
    answer = ''
    def solve(temp,n):
        if n == k:
            return n 
        else:
            for i in temp:
                if i > 0:
                    sliced = temp[:i]+ temp[i+1:]
                
    return answer