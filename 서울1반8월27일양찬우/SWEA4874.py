# SWEA 4874

#SWEA1224 후위계산식 계산기
"""
'(' : 바깥에선 0순위 / 안에선 최하위
')' : 
*/  : 1순위
+-  : 2순위 
int : 바로 출력
"""

import sys
sys.stdin = open('input2.txt','r')
FUNC = {
        "*": lambda x, y: y * x,
        "+": lambda x, y: y + x,
        "-": lambda x, y: y - x,
        "/": lambda x, y: int(y / x),
    }

for T in range(int(input())):
    line = input().split(' ')
    # print(line)
    stack = []
    try:
        for l in range(len(line)):
            if '.' not in line or line[-1] != '.':
                raise EOFError
            if line[l]=='.' and len(stack) >1:
                raise EOFError
            if line[l] == '.':
                print("#{0} {1}".format(T+1, stack.pop()))
            elif line[l].isdigit():
                stack.append(int(line[l]))
            else:
                x, y = stack.pop(), stack.pop()
                stack.append(FUNC[line[l]](x,y))

    except:
        print("#{0} error".format(T+1))
    
