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