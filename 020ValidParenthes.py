class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(': ')', '[':']','{':'}'}
        temp = []
        for ss in s:
            if ss in dic.keys():
                temp.append(ss)
            elif temp and (ss in dic.values() and ss == dic[temp[-1]]):
                temp.pop()
            else:
                return False;
        return not temp

solu = Solution()
print(solu.isValid("()"))

