# 执行用时: 76 ms, 在Contains Duplicate的Python3提交中击败了18.41% 的用户
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for num in nums:
            if d.get(num):
                return True
            else:
                d[num] = True
        return False