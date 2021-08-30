def solution(genres, plays):
    answer = []
    gDict = dict()
    pDict = dict()
    N = len(genres)
    for i in range(N):
        if not pDict.get(genres[i]):
            pDict[genres[i]] = 0
        pDict[genres[i]] += plays[i]
        if not gDict.get(genres[i]):
            gDict[genres[i]] = []
        gDict[genres[i]].append((plays[i],i))
    li = sorted([[v,k] for k,v in pDict.items()])
    while li:
        genre = li.pop()[1]
        genre_list = sorted(gDict[genre])
        check = 0
        while genre_list and check < 2:
            mx,mi,pi = 0,0,0
            for idx,item in enumerate(genre_list):
                if item[0] > mx:
                    mx,mi,pi = item[0],item[1],idx
                elif item[0] == mx:
                    if mi > item[1]:
                        mi = item[1]
                        pi = idx
            answer.append(genre_list.pop(pi)[1])
            check+=1
    return answer


def solution(genres, plays):
    answer = []
    gDict = dict()
    pDict = dict()
    N = len(genres)
    for i in range(N):
        if not pDict.get(genres[i]):
            pDict[genres[i]] = 0
        pDict[genres[i]] += plays[i]
        if not gDict.get(genres[i]):
            gDict[genres[i]] = []
        gDict[genres[i]].append((i,plays[i]))
    for k,v in sorted(pDict.items(),key=lambda x:x[1], reverse=True):
        for i,p in sorted(gDict[k],key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    return answer
# 아래 풀이에서 Line 44~45를 참고했다. sorted에서 기준인 key를 주는 것과 람다를 사용하는 것, 
# 그리고 갯수 상관없이 최대 2개 뽑을 땐 [:2] 해도 괜찮다는 것 기억하기 

"""
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
"""
