def solution(routes):
    answer = 0
    routes.sort(key= lambda x:x[1])
    while routes:
        left,right = routes.pop(0)
        temp = []
        for idx,pos in enumerate(routes):
            if not (pos[0] <= right <= pos[1]):
                temp.append(pos)
        routes = temp        
        answer += 1
    return answer

"""
질문하기에 누가 올려놓은 설명 보고 풀이함. 
모든 기록 중 제일 먼저 고속도로에서 나가는 차의 위치에 무조건 카메라를 설치해야함 
-> 아니면 다른 카메라는 그 차가 나가는 것을 찍지 못할 테니까. 
그리고 해당 카메라가 찍을 수 있는 모든 기록을 제외한 기록 중에서 다시 제일 먼저 나가는 차의 위치에 설치함 
반복한다면 최소 설치 갯수를 구할 수 있다. 
"""