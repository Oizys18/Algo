"""
# 정확도 100퍼, 효율성 0 퍼 
def solution(info, query):
    requirements = [que.replace('and','').replace('-','').split() for que in query]
    applicants = [applicant_info.split() for applicant_info in info]
    cnt = [0]*len(requirements)
    for idx, requirement in enumerate(requirements):
        for person in [x for x in applicants if int(requirement[-1]) <= int(x[-1])]:
            for r in requirement[:-1]:
                if r not in person:
                    break
            else:
                cnt[idx] += 1
    return cnt
"""

info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"]

def solution(info, query):
    Q = len(query)
    I = len(info)
    info = [i.split(' ') for i in info]
    query = [q.replace('and ','').split(' ') for q in query]
    answer = [0]*Q
    for q in range(Q):
        q_data = query[q]
        for i in range(I):
            data =  info[i]
            if int(data[4]) < int(q_data[4]):
                continue
            for idx in range(4):
                if q_data[idx] == '-':
                    continue
                if data[idx] != q_data[idx]:
                    break
            else:
                answer[q] += 1    
    return answer

print(solution(info,query))