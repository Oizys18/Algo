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



def solution(clothes):
    answer = 1
    cloth_dict = dict()
    for item, category in clothes:
        if not cloth_dict.get(category):
            cloth_dict[category] = 1
        else:cloth_dict[category]+= 1
    for v in cloth_dict.values():
        answer *= (v+1) # ?????????????
    return answer-1
