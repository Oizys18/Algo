def my_sum(x, y, k, total_map):
    new_sum = 0
    for i in range(y, y + k, ):
        if i == y or i == y + k - 1:
            for j in range(x, x + k, ):
                new_sum += total_map[i][j]
        else:
            new_sum += total_map[i][x] + total_map[i][x + k - 1]
    return new_sum


def calc_ran(n, m, k, total_map):
    x_ran = m - k + 1
    y_ran = n - k + 1
    result = []
    for y in range(y_ran):
        for x in range(x_ran):
            result.append(my_sum(x, y, k, total_map))
    return result


TC = int(input())
for testcase in range(1, TC + 1):
    # n: 행의 개수  m: 열의 개수 k: 사각 테두리 (계산 기준)
    n, m, k = map(int, input().split())

# 입력 받기
total_map = []
for i in range(n):
    new_lst = list(map(int, input().split()))
    total_map.append(new_lst)

result = calc_ran(n, m, k, total_map)
ge_res = result[0]
for res in result:
    if res > ge_res:
        ge_res = res
print('#{} {}'.format(testcase, ge_res))