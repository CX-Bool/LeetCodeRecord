# 执行用时: 76 ms, 在Remove Duplicates from Sorted Array的Python3提交中击败了83.68% 的用户
# 内存消耗: 8.3 MB, 在Remove Duplicates from Sorted Array的Python3提交中击败了76.32% 的用户
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i,j = 0,0
        n = len(nums)
        while(j<n):
            if nums[j]>nums[i]:
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
            j+=1
        return i+1