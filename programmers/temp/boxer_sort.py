def solution(weights, head2head):
    N = len(weights)
    temp = [i for i in range(N)]
    winRate = [0]*N
    winHeavy = [0]*N
    for x in range(N):
        w,l = 0,0
        for y in range(N):
            if head2head[x][y] == 'W':
                w += 1
                if weights[x] < weights[y]:
                    winHeavy[x] += 1 
            elif head2head[x][y]=='L':
                l += 1 
        if w:winRate[x] = (w/(w+l))

    def condition(i:int,j:int) -> bool:
        if winRate[i] != winRate[j]:
            return winRate[i] < winRate[j]
        if winHeavy[i] != winHeavy[j]:
            return winHeavy[i] < winHeavy[j]
        if weights[i] != weights[j]:
            return weights[i] < weights[j]
        return i > j
    
    for i in range(N-1):
        for j in range(N-i-1):            
            if condition(temp[j],temp[j+1]):
                temp[j],temp[j+1] = temp[j+1],temp[j]

    return [i+1 for i in temp]

# https://programmers.co.kr/learn/courses/30/lessons/85002