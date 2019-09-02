str = "2 + 3 * 4 / 5"

stack = [0] * 10
top = -1
idx = 0
post_exp = [0] * 10

for i in range(len(str)):
    if '*' <= str[i] <= '/':
        top += 1;
        stack[top] = str[i]
    elif '0' <= str[i] <= '9':
        post_exp[idx] = str[i]
        idx += 1

while top != -1 :
    post_exp[idx] = stack[top]
    idx += 1
    top -= 1

print(' '.join(post_exp[:idx]))