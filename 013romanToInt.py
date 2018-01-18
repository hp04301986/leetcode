"""
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
相同的数字连写，所表示的数等于这些数字相加得到的数，如 Ⅲ=3；
小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 Ⅷ=8、Ⅻ=12；
小的数字（限于 Ⅰ、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 Ⅳ=4、Ⅸ=9；
在一个数的上面画一条横线，表示这个数增值 1,000 倍
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

print(Solution.romanToInt(Solution, "MCMXCVI"))