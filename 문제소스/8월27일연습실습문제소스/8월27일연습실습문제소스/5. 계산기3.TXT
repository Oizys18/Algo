import sys
sys.stdin = open("input.txt", "r")

stack = [0] * 200
post_exp = [0] * 200


for tc in range(1, 11):
    N = int(input())
    exp = input()

    top = -1
    idx = 0

    for token in exp:
        if token == '(' :
            top += 1
            stack[top] = '0'
        elif token >= '0':
            post_exp[idx] = token
            idx += 1
        elif token == ')' :
            while stack[top] != '0':
                post_exp[idx] = stack[top]
                idx += 1
                top -= 1
            top -= 1
        else: # '*' ==> 42,  '+' ==> 43
            while top != -1 and token >= stack[top] :
                post_exp[idx] = stack[top]
                idx += 1
                top -= 1
            top += 1
            stack[top] = token

    top = -1
    p_exp = post_exp[:idx]
    for token in p_exp:
        if token >= '0' :
            top += 1
            stack[top]  = int(token)
        elif token == '+':
            top -=1
            stack[top] += stack[top + 1]
        else:
            top -=1
            stack[top] *= stack[top + 1]

    print("#%d"%tc,stack[0])


