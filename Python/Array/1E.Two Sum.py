# Accepted
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            b = target - nums[i]
            if b in nums:
                j = nums.index(b)
                if i != j:
                    res = [i, j]
                    break
        return res