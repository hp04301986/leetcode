"""
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0; p = "I"
        for c in s[::-1]:
            result = result - dic[c] if dic[c] < dic[p] else result + dic[c]
            p = c
        return result