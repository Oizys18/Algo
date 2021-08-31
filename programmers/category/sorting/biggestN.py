"""
# 가장 큰 수


문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	6210
[3, 30, 34, 5, 9]


"""

numbers = [3, 30, 34, 5, 9]
def solution2(numbers):
    from functools import cmp_to_key
    answer = list(map(str,numbers))
    answer.sort(key=cmp_to_key(lambda a,b: int(b+a)-int(a+b)))
    return answer 
print(solution2(numbers))
"""
python functools 라이브러리의 cmp_to_key는 고차함수를 활용하는 방법 
"""




def solution(numbers):
    arr = [x for x in range(1001)]
    count = [y for y in range(1001)]
    answer = ''

    def compare(a, b):
        ab = int(str(a)+str(b))
        ba = int(str(b)+str(a))
        if ab <= ba:
            return True
        else:
            return False

    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if compare(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    for n in range(len(arr)):
        count[n] = numbers.count(arr[n])

    for c in range(len(count)):
        if count[c]:
            answer += str(arr[c])*count[c]

    return str(int(answer))