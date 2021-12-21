class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n:
            if n % 2:
                if n == 1:
                    return True
                else:
                    return False
            n = n//2
