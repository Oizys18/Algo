# GCD 합 
for T in range(int(input())):
    n, *nums = list(map(int,input().split()))
    def GCD(x, y):
        a, b = max(x,y), min(x,y)
        while True:
            r = a % b
            if r == 0:
                return b
            else:
                a = b
                b = r
    gcdSet = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            gcdSet.append(GCD(nums[i],nums[j]))
    print(sum((gcdSet)))


"""
문제 좀 잘 읽자..

"""