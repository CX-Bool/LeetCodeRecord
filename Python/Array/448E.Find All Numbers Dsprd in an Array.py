# 执行用时: 172 ms, 在Find All Numbers Disappeared in an Array的Python3提交中击败了96.52% 的用户
# must using extra space
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        appeared = set(nums)
        all = set(range(1, len(nums)+1))
        dis = all - appeared
        return list(dis)