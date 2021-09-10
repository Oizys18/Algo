def solution(distance, rocks, n):
    rocks.sort()
    rocks = [0] + rocks + [distance]
    arr = [rocks[i]-rocks[i-1] for i in range(1,len(rocks))]

    def binSearch(arr):
        def condition(mid):
            removed = 0
            total = 0
            for i in arr:
                total += i 
                if total <= mid:
                    removed += 1 
                else:
                    total = 0
            
            return removed > n          
        
        left,right = 1,distance 
        while left < right:
            mid = left + (right-left)//2
            if condition(mid):
                right = mid -1
            else:
                left = mid + 1
        return left 
    
    return binSearch(arr)



"""
매우 어려웠다. 
이분탐색인줄도 몰랐고 
풀이 보고도 고민했다. 

사실 아직도 대충 풀이 방법은 이해했는데, 
condition에서 등호 선택이 헷갈린다. 왜 line12에서 <이 아니라 <= 인것이지? 

-> 좀 더 고민해서 깨달았다. 단순한 착각이었는데, 
부등호라고 생각했던 이유는 값이 mid와 같으면 이미 해당 total이 mid값, 즉 최솟값이기 때문에 
뺄 필요가 없다고 생각했다. 
하지만 잘 생각해보면 total은 i까지의 값이고, removed에 추가하는 경우는 i를 더한 값이 mid보다 클 때 더하는 것이다. 
즉 등호의 경우, total이 mid와 같아지려면 결국 i를 
Line 12에서 total은 현재 인덱스까지 더한 값이다. 
"""