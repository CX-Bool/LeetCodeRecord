# 执行用时: 44 ms, 在Merge Sorted Array的Python3提交中击败了99.73% 的用户
# 内存消耗: 6.5 MB, 在Merge Sorted Array的Python3提交中击败了86.92% 的用户
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        j=m-1
        k=n-1
        i=m+n-1
        while i>=0:
            if j< 0 or nums2[k]>nums1[j] and k>=0:
                nums1[i]=nums2[k]
                i-=1
                k-=1
            else:
                nums1[i] = nums1[j]
                i-=1
                j-=1 