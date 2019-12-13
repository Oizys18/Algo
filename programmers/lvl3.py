def solution(genres, plays):
    answer = []
    genreDic = {}
    calDic = {}
    for i in range(len(genres)):
        if genres[i] not in calDic.keys():
            calDic[genres[i]] = 0
        calDic[genres[i]] += plays[i]
        if genres[i] not in genreDic.keys():
            genreDic[genres[i]] = []
        genreDic[genres[i]].append((i, plays[i]))
        
    while True:
        for l in calDic.keys():
            if calDic[l] == max(calDic.values()):
                topG = l
                
        res = 0
        big = 0
        bigs = []
        temp = []

        # print(genreDic[topG])
        while genreDic[topG]:
            for k in genreDic[topG]:
                if k[1] == big:
                    bigs.append(k)
                elif k[1] > big:
                    big = k[1]
                    bigs = [k]
                bigs.sort()
            temp.append(bigs[0][0])
            genreDic[topG].pop(genreDic[topG].index(bigs[0]))
            break
        answer.extend(temp)
        genreDic.pop(topG)
        calDic.pop(topG)
            

    return answer