from itertools import combinations as comb
def solution(orders, course):
    answer = []
    orders = [sorted(i) for i in orders]
    cdict = {}
    for order in orders:
        for n in course:
            for i in comb(order,n):
                if not cdict.get(i):
                    cdict[i] = 1
                else: cdict[i] += 1 
    for n in course:
        mx = 0
        mx_i = []
        for k,v in cdict.items():
            if len(k) ==n and v>=2: 
                if v > mx:
                    mx_i = [''.join(k)]
                    mx = v 
                elif v == mx:
                    mx_i.append(''.join(k))
        answer.extend(mx_i)
    return sorted(answer)