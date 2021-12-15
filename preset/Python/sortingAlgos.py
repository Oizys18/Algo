
# 선택 정렬 O(N^2)
def test_selection_sort():
    """선택 정렬을 이용한 정렬 방법"""
    data = [2, 11, 3, 91, 7, 50, 33]
    length = len(data)
    for i in range(length):
        min_idx = i
        for j in range(i+1, length):
            # 더 작은 최솟값이 있다면, 교환(swap)한다.
            if data[min_idx] > data[j]:
                tmp = data[min_idx]
                data[min_idx] = data[j]
                data[j] = tmp

        print("{} 회차: {}".format(i+1, data))


def pythonic_selection_sort():
    data = [2, 11, 3, 91, 7, 50, 33]
    sorted_data = list()
    while data:  # data 에 값이 없을때까지 반복한다.
        min_num = min(data)  # 리스트 중 `가장 작은 값`을 찾는다.
        data.remove(min_num)  # 데이터에서 `가장 작은 값`을 제거한다.
        sorted_data.append(min_num)


# 삽입 정렬 Insertion Sort O(N^2)
def insertion_sort():
    data = [2, 4, 5, 1, 3]
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]  # 오른쪽으로 밀어준다. (공간 확보)
            j -= 1
            data[j + 1] = key
            # print(key, data)
    return data


def pythonic_insertion_sort():
    data = [2, 4, 5, 1, 3]
    sorted_data = list()
    while data:
        value = data.pop(0)
        n = len(sorted_data)  # value 보다 큰 원소가 없는 경우 맨 뒤로 배치 (default)
        insert_idx = n

        # value 보다 큰 원소를 찾는다.
        for i in range(n):
            if value < sorted_data[i]:
                insert_idx = i
                break
        sorted_data.insert(insert_idx, value)
        # print(value, sorted_data)
    return sorted_data


# 버블소트 O(N^2)
def bubble_sort():
    data = [2, 6, 3, 4, 8, 9, 1, 10]
    n = len(data)
    # for _ in range(n-1):
    #     for i in range(n-1):
    #         if data[i] > data[i+1]:
    #             data[i], data[i+1] = data[i+1], data[i]
    # return data
    for i in range(n):
        for j in range(n):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data


print(bubble_sort())


# 병합정렬 O(N*logN)
def recur(group):
    def _merge_sort(group):  # 종료 조건 설정
        n = len(group)
        if n <= 1:
            return group

        # 그룹 나누기
        mid_idx = n // 2
        group1 = _merge_sort(group[:mid_idx])
        group2 = _merge_sort(group[mid_idx:])

        # 정렬
        result = list()
        while group1 and group2:
            result.append(group1.pop(
                0) if group1[0] < group2[0] else group2.pop(0))
            result.extend(group1)
            result.extend(group2)
            # print(result)
            return result

    data = [38, 27, 43, 3, 9, 82, 10]
    return _merge_sort(data)
