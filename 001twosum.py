"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return [i, nums.index(target-nums[i], i+1)]

nums=[2, 7, 11, 15]
target = 18
print(Solution.twoSum(Solution,nums, target))