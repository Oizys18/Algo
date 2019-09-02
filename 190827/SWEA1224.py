#SWEA1224 후위계산식 계산기
"""
'(' : 바깥에선 0순위 / 안에선 최하위
')' : 
*/  : 1순위
+-  : 2순위 
int : 바로 출력
"""

import sys
sys.stdin = open('input.txt','r')

dic = {'*':2, '+':1, '(':0}
for T in range(1,11):
    s = []
    calc = ''
    L = int(input())
    for i in input():
        if i.isdigit():
            calc += i
        elif i == '(':
            s.append(i)
        elif i == ')':
            while s[-1] != '(':
                calc += s.pop()
            s.pop()
        else:
            while s and dic[s[-1]] >= dic[i]:
                calc += s.pop()
            s.append(i)
    while len(s) != 0:
        calc += s.pop()
    s = []
    FUNC = {
        "*": lambda x, y: y * x,
        "+": lambda x, y: y + x,
    }
    for j in calc:
        if j.isdigit():
            s.append(int(j))
        else:
            x = s.pop()
            y = s.pop()
            s.append(FUNC[j](int(x),int(y)))
    print("#{0} {1}".format(T,s.pop()))