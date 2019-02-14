# 执行用时: 52 ms, 在Missing Number的Python3提交中击败了100.00% 的用户
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (n*(n+1))//2 - sum(nums)