# programmers 2609 최대공약수 최소공배수

a, b = map(int,input().split())
B, S = max(a,b), min(a,b)
li = []
def find(B, S):
    while True:
        r = B % S
        if r == 0:
            return S 
        else:
            li.append(r)
            B = S
            S = r
print(find(B,S))
print((B*S)//find(B,S))



"""
유클리드 호제법
최대공약수 : 큰거를 작은거로 나눠서 
    1) 나머지가 생기면, 이전의 작은거를 다시 나머지로 나눈다.
    2) 만약 나누어 떨어지면 직전의 계산의 작은 값이(나머지가) 최대공약수
최소공배수 : 두 수를 곱한 후 최대공약수로 나누면 최소공배수 

"""