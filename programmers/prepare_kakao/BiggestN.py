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
"""
모든 수가 0부터 1000까지의 수니까, 
아예 처음부터 모든 수를 비교해서 arr에 저장한다. 이후 버블소트를 사용해 문제의 정의대로 대소비교를 한다. 
(지금보니 arr를 1000부터 0으로 거꾸로 저장하면 버블소트가 더 빨리 결과를 내놓을 것 같다. )

이후 numbers 속에 arr의 값이 몇개가 있는지 체크한다. 
체크한 갯수만큼 arr에서 곱해서 answer에 넣어준 다음, 결과 answer를 str(int()) 한다. 

너무 충격적인 코드 
내가 쓴 게 아닌 것 같은데... 너무 똑쟁이 코드다 

"""



"""
아래가 새로 푼 풀이, 
시간초과난다. 
join은 굉장히 느리다.. 
"""
def solution(numbers):
    answer = ''
    N = len(numbers)
    for i in range(N-1,0,-1):
        for j in range(i):
            a,b = str(numbers[j]),str(numbers[j+1])
            if int(a+b) < int(b+a):                
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]    
    return str(int(''.join(map(str,numbers))))


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
"""
다른 사람의 코드. 더 똑쟁이다. str에 x*3을 하면 
최대 1000까지니까 모든 str을 *3해서 비교하면 9는 999, 10은 101010이 되어 문제정의대로 비교가능하다.
(python에서 '999' > '101010'은 True이다. ) 
"""

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
"""
77에서 비교 방법을 functools를 사용했다는 점이 독특하다. 
또한 비교함수에서 등호비교 후 차를 return에서 1,0,-1의 값을 리턴하니까 
sorted의 key로 사용했을 때 좌로 이동 / 정지 / 우로이동이 되는 것 같다. 띠용한 코드 
"""