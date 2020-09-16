# 카카오 블라인드 2020 자물쇠와 열쇠
from pprint import pprint as pp

key = [[0, 0, 0],
       [1, 0, 0],
       [0, 1, 1]]
# key = [[0, 0],
#        [1, 0],]

lock = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]
"""
## 풀이
- M은 항상 N 이하 
    - N행렬에서 (0,N-M+1) 만큼씩 순회 ( 행렬의 크기 )
    - 굳이 1:1로 대응관계를 볼 필요 없다. // key의 값 에서 각 좌표마다 +1 해보면 된다! 
    - 같은 원리로 굳이 key를 잘라서 비교할 필요없이, key에서 x,y 점을 +1 했을 때 map보다 크다면 제외한다.     
"""


def solution(key, lock):
    answer = True
    M = len(key[0])
    N = len(lock[0])
    # sumN = sum(list(map(sum,lock)))p
    # 열쇠회전
    def turn_key(key):
        return list(zip(*key[::-1]))
    # key = turn_key(key)

    # 열쇠가 자물쇠에 맞는가?
    def checkFit():
        pass

    for turn_idx in range(4):
        pp(key)
        # 좌표를 0,N-M+1 까지 순서대로 옮긴다. 
        for a in range(0,N-M+1): # 열 이동
            for b in range(0,N-M+1): # 행 이동
                
                # 좌표지점에서 비교 
                for x in range(M):
                    for y in range(M):
                        

                print('------divider')
        if checkFit():
            return True 
        else:
            # 이번 for가 끝나기 전에 key를 회전한다.
            key = turn_key(key)
    else:
        return False 




print(solution(key, lock))
