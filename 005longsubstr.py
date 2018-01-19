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
        i = 0
        res = s[0]
        l = len(s)
        while i < l:
            j = l
            t = l - i
            while j > i + 1:
                temp = s[i:j]
                if temp == ss[l - j:t] and len(temp) > len(res):
                    res = temp
                j = j - 1
            i = i + 1
        return res

    def longestPalindrome1(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1;
            r += 1
        return s[l + 1:r]

print(Solution.longestPalindrome1(Solution, "ccd"));