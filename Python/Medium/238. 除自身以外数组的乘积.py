class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        res = [1 for _ in range(n)]
        l=r=1
        for i,j in zip(range(n),range(n-1,-1,-1)):
            res[i],l = res[i]*l, l*nums[i]
            res[j],r = res[j]*r, r*nums[j]
        return res
