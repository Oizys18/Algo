def solution(numbers):
    answer = 0
    N = len(numbers)
    nums = set()
    def check_sosu(n):
        if n < 2:return False 
        for i in range(2,n//2+1):
            if not n%i:
                return False 
        else:return True 
    
            
    visit = [0]*(N+1)
    def perm(k,num):
        if k == N and num:
            if int(num) > 1:
                nums.add(int(num))
            return 
        else:
            for i in range(N):
                if visit[i]:
                    continue
                visit[i] = 1 
                perm(k+1,num+numbers[i])
                perm(k+1,num)
                visit[i] = 0
                
    perm(0,'')
    for n in nums:
        if check_sosu(n):
            answer += 1
    return answer