# 执行用时: 56 ms, 在Move Zeroes的Python3提交中击败了99.58% 的用户
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        while j < len(nums):
            nums[j] = 0
            j += 1
# to be improved
# class Solution:
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         i = 0
#         while i < n:
#             if nums[i] == 0:
#                 for j in range(i+1, n):
#                     nums[j-1], nums[j] = nums[j], nums[j-1]
#                 n -= 1
#             else:
#                 i += 1