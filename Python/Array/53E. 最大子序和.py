# 执行用时 : 80 ms, 在Maximum Subarray的Python3提交中击败了15.37% 的用户
# 内存消耗 : 14 MB, 在Maximum Subarray的Python3提交中击败了0.90% 的用户
class Solution:

    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum = [0]*n
        # max_sum[i] 从0开始，包含i位的连续的最大和
        max_sum[0]=nums[0]
        for i in range(1,len(nums)):
            max_sum[i]=max(nums[i], nums[i]+max_sum[i-1])
        return max(max_sum)

        pass