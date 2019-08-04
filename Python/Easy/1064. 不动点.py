class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i,num in enumerate(A):
            if i == num:
                return i
        else:
            return -1