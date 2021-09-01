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
        answer *= (v+1)
    return answer-1

"""
nPr n개에서 r개 뽑아 나열(중복가능) == n!/(n-r)!
nCr n개에서 r개 선택하는 조합 == nPr / r! == n*(n-1)*(n-2)*...*(n-r+1) / r*(r-1)*(r-2)*1

위와 같은 경우 각 카테고리 별 (n+1)C1을 모두 곱해준다음 ==(n개 + 해당 카테고리에서 안고르는 경우)C(1개 고르기)   
아무것도 위장을 안하면 안된다고 하니 (-1)을 해주면 된다. 
"""