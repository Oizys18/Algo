# 6588.py 골드바흐 추측

li = [0]*1000001
sosuli = [0]*1000001
def sosu(num):
    if sosuli[num]:
        return sosuli[num]
    if num == 1:
        return False
    for i in range(2, (num//2) + 1):
        if num % i == 0:
            return False
    sosuli[num] = 1
    return True

while True:
    n = int(input())
    if li[n]:
        print(li[n])
    else:
        if n != 0:
            for i in range(3,n//2 + 1,2):
                if sosu(i) and sosu(n-i):
                    print(f"{n} = {i} + {n-i}")
                    li[n] = f"{n} = {i} + {n-i}"
                    break
            else:
                print("Goldbach's conjecture is wrong.")
        else:
            break