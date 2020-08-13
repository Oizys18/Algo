numbers = [1, 1, 1, 1, 1,1, 1,1, 1]
target = 3


def solution(numbers, target):
    import copy
    answer = 0
    N = len(numbers)
    # 양수값, 음수값 체크
    arr_dict = []
    arr = [0]*N
    visit = [0]*N

    def DFS(K, arr):
        # 끝에 도달
        if K == N:
            if sum(arr) == target:
                print('정답!', arr)
            return
        else:
            for i in range(N):
                if not visit[i]:
                    print(K, arr)
                    visit[K] = 1
                    # K번째 값 + 추가
                    arr[K] = numbers[K]
                    DFS(K+1, arr)
                    visit[K] = 0
                    # K번째 값 - 추가
                    arr[K] = -numbers[K]
                    DFS(K+1, arr)
                    visit[K] = 1

    DFS(0, arr)
    print(visit)
    return answer


print(solution(numbers, target))
