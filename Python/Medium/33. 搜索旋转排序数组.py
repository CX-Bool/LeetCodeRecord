class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        def bisearch(nums, tar, i, j):
            # print('bisearch from %s to %s'%(i,j))
            mid = (i + j) // 2
            val = nums[mid]
            if val == tar:
                return mid
            elif i >= j:
                return -1
            elif tar < val:
                # print('next bisearch for %s from %s to %s'%(tar,i,mid-1))
                return bisearch(nums, tar, i, mid - 1)
            else:
                # print('next bisearch for %s from %s to %s'%(tar,mid+1,j))
                return bisearch(nums, tar, mid + 1, j)

        if nums[-1] >= nums[0]:
            return bisearch(nums, target, 0, len(nums) - 1)

        def find_reverse(nums, i, j):
            # print('search for %s - %s'%(i,j))
            if i == j:
                return i
            mid = (i + j) // 2
            if nums[i] == nums[mid]:
                return i if nums[i] > nums[j] else j
            elif nums[i] < nums[mid]:
                return find_reverse(nums, mid, j)
            else:
                return find_reverse(nums, i, mid - 1)

        r_index = find_reverse(nums, 0, len(nums) - 1)

        # print(r_index)

        if nums[-1] == target:
            return len(nums) - 1
        elif nums[-1] > target:
            return bisearch(nums, target, r_index + 1, len(nums) - 2)
        else:
            return bisearch(nums, target, 0, r_index)