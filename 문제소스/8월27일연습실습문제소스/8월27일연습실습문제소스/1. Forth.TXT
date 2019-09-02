import sys
sys.stdin = open("input.txt", "r")

s = [0] * 100

T = int(input())
for tc in range(1, T+1):
    post_exp = list(input().split())

    print("#%d" % tc, end=' ')
    top = -1
    for x in post_exp:
        if x in ('+', '-', '*', '/') :
            if top < 1 : print('error'); break
            if   x == '*': s[top - 1] *= s[top]
            elif x == '+': s[top - 1] += s[top]
            elif x == '-': s[top - 1] -= s[top]
            elif x == '/': s[top - 1] //= s[top]
            top -= 1
        elif x == '.' :
            if top != 0: print('error')
            else : print(s[0])
        else:
            top += 1
            s[top] = int(x)