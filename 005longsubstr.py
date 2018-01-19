"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example:
Input: "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = s[::-1]
        if s == ss:
            return s
        temp = list()
        i = 0
        while i < len(s):
            print(i)
            l = j = len(s)
            while j > i:
                print(j)
                print("1:::", s[i:j])
                print("2:::", ss[l-j:l-i])
                if s[i:j] == ss[l-j:l-i]:
                    temp.append(s[i:j])
                j = j -1
            i = i + 1
        print(temp)
        temp = sorted(temp, key=lambda x: len(x))
        print(temp)
        return sorted(temp, key=lambda x: len(x))[-1]

print(Solution.longestPalindrome(Solution, "ccd"));