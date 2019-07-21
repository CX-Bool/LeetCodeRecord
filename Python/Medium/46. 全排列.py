'''执行用时 :
36 ms
, 在所有 Python 提交中击败了
64.90%
的用户
内存消耗 :
11.7 MB
, 在所有 Python 提交中击败了
37.46%
的用户'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            head = nums[i:i+1]
            other = nums[:i]+nums[i+1:]
            olist = self.permute(other)
            res += [head+o for o in olist]
        return res