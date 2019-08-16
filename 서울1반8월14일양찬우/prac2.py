# str() 쓰지 않고 itoa() 구현
# 양의 정수 입력받아 문자열로 변환 

# input = 정수값, 변환할 문자열을 저장할 문자배열 


"""
char(48) = 0 
char(57) = 9
"""

a= 1148

def itoa(n):
    str_num = ''
    while True:
        tmp = n % 10 
        n -= tmp 
        n = int(n / 10)
        str_num = chr(48+tmp) + str_num
        if n/10 < 1 :
            str_num = chr(48+tmp) + str_num
            break
    return str_num

print(itoa(a))

