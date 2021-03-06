"""
Given an integer, write a function to determine if it is a power of three.
Follow up:
Could you do it without using any loop / recursion?
"""
#由于输入是int，正数范围是0-231，在此范围中允许的最大的3的次方数为319=1162261467，那么我们只要看这个数能否被n整除即可。
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n >= 1 and 1162261467 % n == 0

s = Solution()
print(s.isPowerOfThree(243))