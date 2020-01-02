import itertools

L, C = map(int,input().split())
words = list(input().split())
vowel = []
consonent = []
for i in words:
    if i in 'aeiou':
        vowel.append(i)
    else:
        consonent.append(i)


print(vowel)
print(consonent)
