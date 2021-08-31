def solution(n, lost, reserve):
    answer = 0
    student = [1]*n
    for l in lost:
        student[l-1] -= 1 
    for r in reserve:
        student[r-1] += 1 
    
    for i in range(0,n):
        if student[i] == 2:
            if i == 0:
                if student[i+1] == 0:
                    student[i+1] += 1
                    student[i] -= 1
            if i == n-1:
                if student[i-1] == 0:
                    student[i] -=  1
                    student[i-1] += 1
            else:
                if student[i-1] == 0:
                    student[i] -=  1
                    student[i-1] += 1
                elif student[i+1] == 0:
                    student[i+1] += 1
                    student[i] -= 1
    for k in student:
        if k:
            answer += 1
    return answer


# 다시 푼 풀이  
def solution(n, lost, reserve):
    temp = [1]*n
    for l in lost:
        temp[l-1] -= 1 
    for r in reserve:
        temp[r-1] += 1
    for i,t in enumerate(temp):
        if t==2:
            if i > 0 and not temp[i-1]:
                temp[i]-=1
                temp[i-1] = 1
            elif i<n-2 and not temp[i+1]:
                temp[i] -=1
                temp[i+1] = 1
    return n-temp.count(0)


# 또 다시 푼 풀이 
def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    for student in reserve:
        if student in lost:
            lost.remove(student)
        else:
            if student-1 in lost:
                lost.remove(student-1)
            elif student+1 in lost and student+1 not in reserve:
                lost.remove(student+1)
    return n-len(lost)

"""
Line 55~56 + Line 59~62의 방법이 안통해서 Line 33의 방법으로 다시 풀었었다. 
하지만 이 방법이 안통하는 이유를 모르겠어서 결국 다시 풀었음. 
생각해보니까 lost와 reserve가 sort되어있는 상태에서만 통하는 방법이었다. 
-> 내 체육복을 잃어버렸는데 내가 체육복이 있다면 무조건 난 아무에게도 못 빌려준다 
-> 즉, Line 61에서 student+1 not in reserve로 체크해줘야 한다. 
-> 이 로직에서 만약 다음 학생이 본인이 도둑맞았는데 체육복이 있는 사람이라면, 
-> 원래대로라면 아무에게도 안빌려주지만 앞선 학생이 해당 학생에게 빌려줘버리면 
-> Line 56에서 조건문에 안걸리고 본인은 체육복이 있는 것으로 생각해서 다른 사람에게 체육복을 빌려주게 된다. 

"""