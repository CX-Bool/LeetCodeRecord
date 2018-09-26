# Accepted
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