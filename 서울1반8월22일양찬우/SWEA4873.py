#SWEA 4873

import sys
sys.stdin = open('input.txt','r')


for T in range(int(input())):
    word = list(input())
    stack = []
    for i in range(len(word)):
        if not stack or stack[-1] != word[i]:
            stack.append(word[i])
        elif stack and stack[-1] == word[i]:
            stack.pop()
    print("#{0} {1}".format(T+1, len(stack)))