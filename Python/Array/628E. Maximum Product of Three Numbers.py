# 执行用时: 136 ms, 在Maximum Product of Three Numbers的Python3提交中击败了29.76% 的用户
# 内存消耗: 7.5 MB, 在Maximum Product of Three Numbers的Python3提交中击败了98.95% 的用户
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])