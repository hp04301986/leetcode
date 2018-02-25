"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
"""
import re

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = re.sub("\W", "", s.strip())
        if not ss or len(ss) == 1:
            return True
        l = list(ss.lower())
        l.reverse()
        rss = "".join(l)
        if ss.lower() == rss:
            return True
        return False

sol = Solution()
print(sol.isPalindrome("ab"))
