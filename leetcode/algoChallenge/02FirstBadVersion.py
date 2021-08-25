# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1 2 3 4 5 6 7 8 9 
        
        
        def checkBV(pre,nxt):
            if isBadVersion(pre) and isBadVersion(nxt):
                return checkBV(nxt,nxt//2)
            elif isBadVersion(pre) and not isBadVersion(nxt) and pre-nxt>1:
                return checkBV(pre,(pre-nxt)//2+nxt)
            elif isBadVersion(pre) and not isBadVersion(nxt) and pre-nxt == 1:
                return pre 
        return checkBV(n,n//2)