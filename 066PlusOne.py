"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.
"""

from functools import reduce
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        num = reduce(lambda x, y: x*10 + y, digits) + 1
        return [int(i) for i in str(num)]

sol = Solution
print(sol.plusOne(sol, [0]))