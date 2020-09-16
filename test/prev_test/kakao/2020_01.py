# 문자열 압축
"""
문자열 처리 
비손실 압축
가장 긴 반복 문자열 검색 후 압축 
-> 가장 효율 좋은 압축방법 탐색 
완전탐색을 통해 
1 <= n < len(s) 길이 n 변수로 
압축 단위를 늘려나가며 압축시도, 
이후 압축 효율이 제일 큰 단위 선택 후 가장 짧은 것 return 
"""
s = "aabbaccc"
# n=1 
#    2 2 1 3 
def solution(s):
    answer = 0
    line_length = len(s)

    # for 문을 돌리면 최소 가능
    compression_n = 1
    while True:
        # slice word with the length compression_n
        # check if the word is repeatitive
        visited = [0]*line_length
        for idx in range(line_length):
            
            # 압축 결과물
            compressed_line = ''
            sliced_cnt = 1

            # 범위 넘어가는 경우
            if idx + compression_n > line_length:
                continue
            sliced_word = s[idx:idx+compression_n]
            for check_idx in range(idx+compression_n, line_length-compression_n+1):
                if visited[check_idx]:
                    continue
                if sliced_word == s[check_idx:check_idx+compression_n]:
                    visited[check_idx] = 1
                    sliced_cnt += 1
                    print('same!')
                    print(sliced_cnt,sliced_word)
                else:
                    break
        break
    print(visited)

                # # 현재 순서 문자열과 이전 문자열 비교함수 / 추가
                # def checkWord(pre, cur):
                #     if pre == cur:
                #         return True
                #     else:
                #         return False

    return answer


print(solution(s))


# 괄호변환
"""
문자열 처리 
전형적인 올바른 괄호 찾기 문제 + 조건 추가 
"""

# 자물쇠와 열쇠
"""
배열 + 시뮬레이션 문제 
열쇠와 자물쇠 조건 함수 + 배열 범위 함수 필요 

"""

# 가사검색
"""
정확성 + 효율성 테스트...!
문자열 처리 / 문자열 매칭 

해쉬 필요 
문자열 -> 비트 변환 -> 위치 별로 비교 ! 

"""


# 기둥과 보 설치
"""
BFS + 조건  + 시뮬레이션 

"""

# def Welcome():
#     viewers = '시청자'
#     if viewers:
#         print(f'반가워요 {viewers}')

# Welcome()
