paran1 = '()()((()))'
paran2 = '((()((((()()((()())((())))))'
stack = []

def push(a):
    stack.append(a)


def pop():
    if len(stack)==0:
        #underflow
        return
    else:
        return stack.pop(-1)

for i in paran1:
    if i == '(':
        push(i)
    elif i == ')':
        pop()

if len(stack) != 0:
    print('조건1 위반')
elif len(stack) == 0:
    print('짝맞음')



"""
str1 = '()()((()))'
str = '((()((((()()((()())((())))))'


#flag
wrong = 0
#stack
for i in range(len(str)):
    if str[i] == '(':
        top += 1; stack[top] = str[i]
    elif str[i] == ')':
        if top == -1:
            wrong = 1
            break
        if stack[top] == '(':
            top -= 1

"""