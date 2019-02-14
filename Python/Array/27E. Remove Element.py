# 执行用时: 44 ms, 在Remove Element的Python3提交中击败了99.73% 的用户
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] == val:
                nums[i],nums[j] = nums[j],nums[i]
                j-=1
            else:
                i+=1
        return j+1