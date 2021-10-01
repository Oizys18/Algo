import sys
sys.setrecursionlimit(100000)
def find(number, room):
    if number not in room:
        room[number] = number + 1
        return number
    empty = find(room[number], room)
    room[number] = empty + 1
    return empty
    
def solution(k, room_number):
    answer = []
    room = {}
    for i in room_number:
        num = find(i, room)
        answer.append(num)
    return answer

"""
https://velog.io/@ansrjsdn/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level4-%ED%98%B8%ED%85%94-%EB%B0%A9-%EB%B0%B0%EC%A0%95-Python
https://programmers.co.kr/learn/courses/30/lessons/64063

disjoint set 문제. 
제일 처음엔 dict와 while문으로 현재 number보다 큰 값을 체크해주면서 계산해서 시간초과, 
그 다음엔 고객 리스트 + 방 상태 리스트 2개를 만들어서 상태를 업데이트하며 체크했는데 시간초과 걸렸다. 

현재 빈 방을 검색하고, 만약 현재 number에 방이 비었다면 해당 방을 다음 방으로 연결하고 저장한다. 
(이 때 연결된 바로 다음방 (number+1)이 사실 비어있지 않더라도 상관없다. 이후 line7에서 재귀를 통해 끝까지 검색되기 때문)

만약 방이 비어있지 않다면, 재귀를 통해 비어있는 방을 탐색한다. 
비어있는 방을 찾았다면 처음 검색했던 number를 비어있던 방의 다음방으로 연결해주고 비어있던 방을 return한다. 
이렇게 하면 어떤 방을 find해도 비어있는 방과 연결된다. 
"""