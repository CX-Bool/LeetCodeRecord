class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        if nums[0]*nums[-1]>0:
            return
        res=[]
        n=len(nums)
        for i in range(0,n-2):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            if nums[i]>0:
                break
            l = i+1
            r = n-1
            while l<r:
                # print(i,l,r)
                if nums[i]*nums[r]>0:
                    break
                s = nums[i]+nums[l]+nums[r]
                if s == 0:
                    res.append([nums[i],nums[l],nums[r]])
                if s<0:
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                else:
                    r-=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
        return res