def solution(number, k):
    answer = ''
    end = len(number) - k
    p = 0
    check = 0
    temp = []
    while len(temp) != end:
        big = '0'
        for i in range(p,p+k+1): 
            if big < number[i]:
                big = number[i]
                check = i
                if number[i] == '9':
                    break
        
        
        if big =='0':
            check = p 
        temp.append(number[check])
        k -= check - p
        p = check + 1 
        # print(check,p,k)
    answer = ''.join(temp)
    return answer


#새로 푼 것, 시간초과 + 실패 
def solution(number, k):
    answer = ''
    while k>0:
        for i in range(len(number)):
            a = number[:i]+number[i+1:]
            if number < a:
                number = a
                break
        else:
            number = number[1:]
        k-=1 
    answer = number 
    return answer