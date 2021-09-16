# https://programmers.co.kr/learn/courses/30/lessons/86048?language=python3
def solution(enter, leave):
    answer = [0]*len(enter)
    idx = 0 
    inout = enter.copy()
    while leave:
        l = leave.pop(0)
        if inout.index(l)+1 >= idx:
            idx = inout.index(l)+1
            inout.insert(idx,l)
        else:
            inout.insert(idx,l)
        idx +=1 

    for i in enter:
        room = set()
        flag = 0
        for j in inout:
            if i != j:
                if j not in room:
                    room.add(j)
                else:
                    if not flag:
                        room.remove(j)
            else:
                if not flag:
                    flag = 1 
                else:
                    answer[i-1] = len(room)
    return answer



"""
다른사람
"""
def solution(enter, leave):
    answer = [0] * len(enter)

    room = []
    e_idx = 0
    for l in leave:
        while l not in room:
            room.append(enter[e_idx])
            e_idx += 1
        room.remove(l)
        for p in room:
            answer[p - 1] += 1
        answer[l - 1] += len(room)

    return answer
