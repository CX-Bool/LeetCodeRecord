# 执行用时: 44 ms, 在Two Sum的Python3提交中击败了99.77% 的用户
# 内存消耗: 7.7 MB, 在Two Sum的Python3提交中击败了53.80% 的用户
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        s = set(nums)
        for i in range(len(nums)):
            b = target - nums[i]
            if b in s:
                j = nums.index(b)
                if i != j:
                    res = [i, j]
                    break
        return res