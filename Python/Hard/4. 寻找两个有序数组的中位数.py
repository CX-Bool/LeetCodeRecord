class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            # print(int((len(nums2)+0.5)//2), int((len(nums2)-0.5)//2))
            return float((nums2[int((len(nums2) + 0.5) // 2)] + nums2[int((len(nums2) - 0.5) // 2)])) / 2
        if not nums2:
            return float((nums1[int((len(nums1) + 0.5) // 2)] + nums1[int((len(nums1) - 0.5) // 2)])) / 2
        l1 = len(nums1)
        l2 = len(nums2)

        if (l1 + l2) % 2 == 1:
            left = right = (l1 + l2) / 2 + 1
        else:
            left = right = (l1 + l2) / 2
            # right=(l1+l2)/2+1
        # print(left,right)
        res1 = 0
        i = j = 0
        for _ in range(left):
            if i < l1 and j < l2:
                if nums1[i] < nums2[j]:
                    res1 = nums1[i]
                    i += 1
                else:
                    res1 = nums2[j]
                    j += 1
            elif i < l1:
                res1 = nums1[i]
                i += 1
            else:
                res1 = nums2[j]
                j += 1
            # print('left',_,res1)
        i = l1 - 1
        j = l2 - 1
        res2 = 0
        for _ in range(right):
            # print(res2)
            if i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    res2 = nums1[i]
                    i -= 1
                else:
                    res2 = nums2[j]
                    j -= 1
            elif i > 0:
                res2 = nums1[i]
                i -= 1
            else:
                res2 = nums2[j]
                j -= 1
        # print(res1,res2)
        return (float(res1) + float(res2)) / 2
