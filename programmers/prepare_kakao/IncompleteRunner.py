"""def solution(participant, completion):
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
"""


def solution(participant, completion):
    answer = ''
    runners_dict = {}
    for runner in participant:
        if not runners_dict.get(runner):
            runners_dict[runner] = 0
        runners_dict[runner] += 1 
    for runner in completion:
        runners_dict[runner] -= 1 
    for k,v in runners_dict.items():
        if v:
            answer = k
    return answer



"""
# 다른사람 코드. 
# Counter 객체는 뺄셈이 가능 

import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""