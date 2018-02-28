"""
Given an integer, write a function to determine if it is a power of two.
"""
import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n >= 1:
            if math.log2(n).is_integer():
                return True
        return False
s = Solution()
print(s.isPowerOfTwo(-1))