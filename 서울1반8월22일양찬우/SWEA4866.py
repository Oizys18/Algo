#SWEA 4866

import sys
sys.stdin = open('input.txt','r')


def Test(line):
    stack = []
    result = 0
    for n in line:
        if (n == '}' or n == ')') and len(stack) == 0 :
            return 0
        if n == '(' or n == '{':
            stack.append(n)
            continue
        elif n == ')':
            top = stack.pop()
            if top == '(':
                result = 1
                continue
            else:
                return 0
        elif n == '}':
            top = stack.pop()
            if top == '{':
                result = 1
                continue
            else:
                return 0
        else:
            continue
    if len(stack) > 0 :
        return 0
    return result


for T in range(int(input())):
    line = input()
    # print(line[0])
    res = 0
    print("#{0} {1}".format(T+1,Test(line)))


        
    
    