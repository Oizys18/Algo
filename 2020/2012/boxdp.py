def solution(n):
    temp = [0]*(n)
    temp[0] = 1 
    temp[1] = 2
    for x in range(2,n):
        temp[x] = (temp[x-2] + temp[x-1]) % 1000000007
    return temp[n-1]