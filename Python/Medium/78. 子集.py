'''执行用时 :
24 ms
, 在所有 Python 提交中击败了
88.07%
的用户
内存消耗 :
11.8 MB
, 在所有 Python 提交中击败了
36.31%
的用户'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums,[]]
        sub = self.subsets(nums[1:])
        head = nums[0:1]
        return sub+[head+s for s in sub]