class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        def bisearch(tar, l, r):
            mid = (l + r) // 2
            val = nums[mid]
            if tar == val:
                return True
            elif l >= r:
                return False
            elif nums[l] < val:
                # 左边是升序
                if nums[l] <= tar < val:
                    return bisearch(tar, l, mid - 1)
                else:
                    return bisearch(tar, mid + 1, r)
            elif val < nums[r]:
                # 右边是升序
                if val < tar <= nums[r]:
                    return bisearch(tar, mid + 1, r)
                else:
                    return bisearch(tar, l, mid - 1)
            elif nums[l] == val:
                return bisearch(tar, l + 1, r)
            elif nums[r] == val:
                return bisearch(tar, l, r - 1)

        return bisearch(target, 0, len(nums) - 1)
