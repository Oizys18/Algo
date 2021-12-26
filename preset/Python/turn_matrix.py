from pprint import pprint as pp
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# 기본 행렬
"""
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
"""
pp(matrix)

# 행렬 y축 뒤집기
"""
[[7, 8, 9],
 [4, 5, 6],
 [1, 2, 3]]
"""
pp(matrix[::-1])

# 행렬 x <-> y 축변환
"""
[[1, 4, 7], 
 [2, 5, 8], 
 [3, 6, 9]]
"""
pp(list(map(list, zip(*matrix))))

# 행렬 x <-> y 축변환 + y축 뒤집기
"""
[[3, 6, 9],
 [2, 5, 8],
 [1, 4, 7]]
"""
pp(list(map(list, zip(*matrix)))[::-1])

# 행렬 x <-> y 축변환 + y축 뒤집기 + x축 뒤집기
"""
[[9, 6, 3],
 [8, 5, 2],
 [7, 4, 1]]
"""
pp(list(map(list, zip(*matrix[::-1])))[::-1])
