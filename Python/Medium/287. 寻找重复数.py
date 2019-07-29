class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for x in nums:
            if x not in s:
                s.add(x)
            else:
                return x