class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check(start,end):
            mid = (end-start)//2 +start
            if mid ==start:
                return mid,end
            if nums[mid] < target:
                return check(mid,end)
            elif nums[mid] > target:
                return check(start,mid)
            else: return mid,end
                
        
        N = len(nums)
        if N == 1:
            if nums[0] == target:
                return 0
            return -1 
        else:
            start,end = check(0,N-1)
            if nums[start]==target: return start
            if nums[end]==target:return end
            return -1 
        
