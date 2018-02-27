"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""
import string
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        while n > 0:
            result.append(string.ascii_uppercase[(n-1) % 26])
            n = (n-1) // 26
        result.reverse()
        return ''.join(result)

s = Solution()
print(s.convertToTitle(1))
