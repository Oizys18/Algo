class NumArray:

    def __init__(self, nums):
        self.arr = nums 
        

    def sumRange(self, left, right) -> int:
        print(self.arr[left:right+1])
        return sum(self.arr[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

numArray = NumArray([-2, 0, 3, -5, 2, -1])
