"""
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 0
        while n > 0:
            n //= 5
            print(n)
            r += n
        return r

s = Solution()
print(s.trailingZeroes(15))
