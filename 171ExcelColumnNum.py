"""
Related to question Excel Sheet Column Title
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""
import string
from functools import reduce
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y: x * 26 + y, map(lambda x: ord(x) - ord('A') + 1, "AB"))

m = map(lambda x: ord(x) - ord('A') + 1, "AB")
for mm in m:
    print(mm)
result = reduce(lambda x, y: x * 26 + y, map(lambda x: ord(x) - ord('A') + 1, "AB"))
print(result)