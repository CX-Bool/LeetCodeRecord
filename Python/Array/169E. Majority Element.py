# 执行用时: 56 ms, 在Majority Element的Python3提交中击败了98.84% 的用户
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]