"""
Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a

        return bin(int(a, 2) + int(b, 2))[2:]


sol = Solution
print(sol.addBinary(sol, "10", "11"))