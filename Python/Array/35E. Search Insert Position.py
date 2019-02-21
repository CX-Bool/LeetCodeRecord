# 执行用时: 72 ms, 在Search Insert Position的Python3提交中击败了4.53% 的用户
# 内存消耗: 7.2 MB, 在Search Insert Position的Python3提交中击败了86.81% 的用户
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i,n in enumerate(nums):
            if n >= target:
                return i
        else:
            return len(nums)