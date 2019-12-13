import itertools
def solution(clothes):
    answer = 1
    wardlobe = {}
    for cloth in clothes:
        if cloth[1] not in wardlobe.keys():
            wardlobe[cloth[1]] = []
        wardlobe[cloth[1]].append(cloth[0])
    for j in wardlobe.keys():
        answer *= (len(wardlobe[j])+1)
    answer -= 1 
    return answer