# 执行用时: 120 ms, 在Array Partition I的Python3提交中击败了99.62% 的用户

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        odd_nums = nums[::2]
        return sum(odd_nums)