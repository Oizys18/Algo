def solution(participant, completion):
    mara = {}
    for i,x in enumerate(completion):
        if x not in mara.keys():
            mara[x] = 0
        mara[x] += 1
    
    for j in participant:    
        if j in mara.keys():
            if mara[j] == 0:
                answer = j
                break
            else:
                mara[j] -= 1
        else:
            answer = j
            break
    
    return answer