#Accepted

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        odd_nums = nums[::2]
        return sum(odd_nums)