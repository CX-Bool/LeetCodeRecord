# Accepted
# to be improved
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                for j in range(i+1, n):
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                n -= 1
            else:
                i += 1