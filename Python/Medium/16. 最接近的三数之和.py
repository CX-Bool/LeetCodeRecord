class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        nums = [x-float(target)/3 for x in nums]
        # print(nums)
        pos_dif=1e10
        neg_dif=-1e10
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j < k:
                s = nums[i]+nums[j]+nums[k]
                # print(s,i,j,k)
                if abs(s)<1e-10:
                    return target
                elif s<0:
                    j+=1
                    if s > neg_dif:
                        neg_dif = s
                elif s>0:
                    k-=1
                    if s < pos_dif:
                        pos_dif = s
        print(neg_dif,pos_dif)
        if -neg_dif<pos_dif:
            return int(target+round(neg_dif))
        else:
            return int(target+round(pos_dif))