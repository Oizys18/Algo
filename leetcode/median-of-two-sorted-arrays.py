from numpy import median as npm
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return npm(nums1+nums2)

#  numpy 안쓰고 한번 직접 만들어 봤음. 그런데 오히려 느리거나 비슷하더라 
#         m = len(nums1) 
#         n = len(nums2)
#         center = int((m+n)/2)
#         sumList = sorted(nums1+nums2)
#         if (m+n)%2:
#             return sumList[center]
#         else:
#             return (sumList[center-1] + sumList[center])/2

            