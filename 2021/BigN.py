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
    answer = ''.join(temp)
    return answer

"""
고생했다..
집중력 떨어져서 더더욱.. ㅠ 

포인트 1)
slice를 사용하면 효율이 떨어진다. 
포인트 2) 
python에서 string 형태 숫자끼리 대소 비교 가능 -> 굳이 int로 형변환할 필요없음 
포인트 3) 
index만을 움직이면서 계산하면 된다. 
포인트 4) 
'9'는 넘어가도록 예외처리 

"""