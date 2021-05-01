import sys
sys.stdin=open('BOJ1157.txt','r')

wd = dict()
for w in input():
    w = w.upper()
    if not wd.get(w):
        wd[w] = 0
    wd[w] += 1

cnt = 0
key = ''
for k,v in wd.items():
    if v > cnt:
        cnt = v 
        key = k
    elif v == cnt and cnt:
        key = '?'
print(key)
