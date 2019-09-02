import sys
sys.stdin = open("input.txt", "r")

stack = [0] * 100
top = -1

def solve():
    global top
    for i in range(len(str)):
        if str[i] == '{' or str[i] == '(':
            stack[top + 1] = str[i]
            top += 1
        elif str[i] == '}' or str[i] == ')' :
            if top == -1 : return 0
            if (str[i] == '}' and stack[top] == '(') or (str[i] == ')' and stack[top] == '{'):
                return 0
            top -= 1

    if top == -1 : return 1
    else : return 0

T = int(input())
for tc in range(1, T+1):
    s = list()
    str = input()

    print('#%d'%tc, solve())
    top = -1

