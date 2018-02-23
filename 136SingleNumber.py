"""
Given an array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
from collections import Counter
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = Counter(nums)
        for k, i in a.items():
            print(k)
            print(i)
            if i < 2:
                return k

sol = Solution()
sol.singleNumber([2, 2, 2, 3])