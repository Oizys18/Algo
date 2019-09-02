import sys
sys.stdin = open("input.txt", "r")

stack = [0] * 1000
top = -1

T = int(input())
for tc in range(1, T+1):
    str = input()

    top += 1;    stack[top] = str[0]

    for i in range(1, len(str)):
        if stack[top] == str[i] : top -= 1
        else : top += 1;    stack[top] = str[i]

    print('#%d'%tc, top+1)
    top = -1
