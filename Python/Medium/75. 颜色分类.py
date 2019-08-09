class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        i=0
        n=len(nums)
        j=n-1
        while i<j:
            if nums[i]==0:
                i+=1
            elif nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            else:
                j-=1
        j=n-1
        while i<j:
            if nums[i]==1:
                i+=1
            elif nums[j]==1:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            else:
                j-=1
        return

# 算法
#
# 初始化0的最右边界：p0 = 0。在整个算法执行过程中 nums[idx < p0] = 0.
#
# 初始化2的最左边界 ：p2 = n - 1。在整个算法执行过程中 nums[idx > p2] = 2.
#
# 初始化当前考虑的元素序号 ：curr = 0.
# 
# While curr <= p2 :
#
# 若 nums[curr] = 0 ：交换第 curr个 和 第p0个 元素，并将指针都向右移。
#
# 若 nums[curr] = 2 ：交换第 curr个和第 p2个元素，并将 p2指针左移 。
#
# 若 nums[curr] = 1 ：将指针curr右移。