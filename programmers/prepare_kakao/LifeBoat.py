# 시간초과
def solution(people, limit):
    answer = 0
    N = len(people)
    people.sort()
    people = [(idx,weight) for idx,weight in enumerate(people)]
    
    pair =[[i[1]]*N for i in people]
    for i1,w1 in people:
        for i2,w2 in people:
            if i1!=i2 and w1+w2 <= limit:
                pair[i1][i2] += w2

    saved = set()
    while len(saved) != N:
        for x in range(N):
            if x not in saved:
                mx = 0
                mi = 0
                for y in range(N):
                    if y not in saved:
                        if pair[x][y] > mx:
                            mx = pair[x][y]
                            mi = y
                answer += 1
                saved.add(x)
                saved.add(mi)
                                            
    return answer 

# 시간초과 2 
def solution(people, limit):
    answer = 0
    N = len(people)
    people.sort()
    saved = [0]*N 
    for i in range(N):
        if not saved[i]:
            temp = people[i]
            for j in range(N-1,0,-1):
                if not saved[j]:
                    if people[j]+temp <= limit:
                        saved[i] = 1
                        saved[j] = 1 
                        answer += 1 
                        break
            else:
                saved[i] = 1 
                answer += 1 
    return answer 

"""
>> N의 최대 길이는 50,000 이다. 
이중 for문의 경우 50000*50000 = 2500000000  즉 25억이 나온다. 
"""


# 통과
def solution(people, limit):
    answer = 0
    N = len(people)
    people.sort()
    
    start = 0
    end = N-1
    saved = [0]*N
    while start<end or sum(saved)!=N:
        if people[start] + people[end] <= limit:
            saved[start] = 1 
            saved[end] = 1
            start += 1
            end -= 1 
        else:
            saved[end] = 1 
            end -= 1 
        answer += 1 
    return answer
"""
애초에 가장 무거운 사람과 가장 가벼운 사람을 짝지어서 태워보내는 것이 greedy 하게 좋은 방법이다. 
이때 만약 가장 가벼운 사람과 가장 무거운 사람을 골랐는데 limit보다 무거우면, 가장 무거운 사람은 다른 누구와도 짝을 지어도 
limit보다 크다는 뜻이니까 혼자 태워서 보내버리면 된다. 
"""


"""
다른사람 코드 보고 보완함 
포인터 2개로 비교하고 while을 돌리는 것은 같으나, 
saved를 통해 체크하는 대신 return이 달라졌다. 
start와 end가 limit보다 작으면 짝을 지을 수 있고, 
그렇게 전부 짝짓고 난 후 전체 사람수에서 짝지은 수를 빼면 보트 수가 나온다. (충격!)
"""
def solution(people, limit):
    answer = 0
    N = len(people)
    people.sort()

    start = 0
    end = N-1
    while start<end:
        if people[start] + people[end] <= limit:
            start += 1
            answer += 1 
        end -= 1 
    return N - answer

