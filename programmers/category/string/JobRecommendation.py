def solution(table, languages, preference):
    answer = ''
    spl_table = [scores.split(' ') for scores in table]
    total = [0]*5
    for job in range(5):
        for i in range(len(languages)):
            if languages[i] in spl_table[job]:
                total[job]+= (6-spl_table[job].index(languages[i]))*preference[i]
    ans = []
    for t in range(5):
        if total[t] == max(total):
            ans.append(spl_table[t][0])
    ans.sort()
    answer = ans[0]                
    return answer