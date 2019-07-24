class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # print(nums,k)
        if not nums:
            return
        if len(nums) == 2:
            return max(nums) if k == 1 else min(nums)
        i = 0
        j = len(nums) - 2
        key = nums[-1]
        while i < j:
            if nums[i] > key:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            elif nums[j] < key:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                i += 1
                j -= 1

        if nums[i] < key:
            i += 1
        smaller = nums[:i]
        larger = nums[i:len(nums) - 1]
        # print(smaller,larger,key,i)
        if not larger:
            if k == 1:
                return key
            return self.findKthLargest(smaller, (k - 1))
        n = len(larger)
        if n == k - 1:
            return key
        elif n > k - 1:
            return self.findKthLargest(larger, k)
        else:
            return self.findKthLargest(smaller, (k - n - 1))