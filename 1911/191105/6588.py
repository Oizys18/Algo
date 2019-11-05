# 6588.py 골드바흐 추측
# def sosu(num):
#     if sosuli[num]:
#         return sosuli[num]
#     if num == 1:
#         return False
#     for i in range(2, (num//2) + 1):
#         if num % i == 0:
#             return False
#     sosuli[num] = 1
#     return True

# sosuli = [0]*1000001
# for i in range(2,1000001):
#     sosu(i)

# while True:
#     n = int(input())
#     if n != 0:
#         for i in range(3,n//2 + 1,2):
#             if sosuli[i] and sosuli[n-i]:
#                 print(f"{n} = {i} + {n-i}")
#                 break
#         else:
#             print("Goldbach's conjecture is wrong.")
#     else:
#         break

"""
에라토스테네스의 체를 사용해야한다..
미리 소수리스트를 다 만들어놓고 가야한다.. 

에라토스테네스의 체를 사용하지 않으면 소수리스트 만들기가 너무 오래걸림
"""
maxNum = 1000001
prime = [0]*maxNum

for i in range(2, maxNum//2):
    if i*i > maxNum:
        break
    if prime[i] == 0:
        for j in range(i*i, maxNum, i):
            prime[j] = 1

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(2, maxNum):
        if prime[i] == 0:
            j = n - i
            if prime[j] == 0:
                print(n, "=", i, "+", j)
                break