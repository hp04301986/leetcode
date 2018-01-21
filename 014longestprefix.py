"""
Write a function to find the longest common prefix string amongst an array of strings.
 seems that it is not to check between pair of strings but on all the strings in the array.
For example:

{"a","a","b"} should give "" as there is nothing common in all the 3 strings.
{"a", "a"} should give "a" as a is longest common prefix in all the strings.
{"abca", "abc"} as abc
{"ac", "ac", "a", "a"} as a.
Logic goes something like this:
Pick a character at i=0th location and compare it with the character at that location in every string.
If anyone doesn't have that just return ""
Else append that character in to the result.
Increment i and do steps 1-3 till the length of that string.
return result.
Make sure proper checks are maintained to avoid index out of bounds error.
"""
from functools import reduce
class Solution:
    def lcp(self, str1, str2):
        i = 0
        while (i < len(str1) and i < len(str2)):
            if str1[i] == str2[i]:
                i = i+1
            else:
                break
        return str1[:i]

    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        else:
            return reduce(self.lcp,strs)
