# 소수 찾기
N = int(input())
li = list(map(int,input().split()))
res = []
def sosu(num):
    flag = 0
    if num == 1:
        return False
    for i in range(2, (num//2) + 1):
        if num % i == 0:
            flag = 1
    if flag:
        return False
    else:
        res.append(num)
        return True
for j in li:
    sosu(j)
print(len(res))


"""
이전에 읽은 소수찾기 블로그 글이 도움이 되었다.
N을 검사할 때 
N//2 이상의 수는 나눠서 검사안해봐도 
어차피 몫이 2~ N//2 사이에 있기 때문에 반만 검사해보면 된다.
더 효율화 시키는 것도 본 것 같은데 이것만 해도 충분한듯 

근데 range 설정에서 2 ~ num//2 + 1 까지 안하고 1 ~ num//2로해서 틀렸다
으이구 멍-청  
"""