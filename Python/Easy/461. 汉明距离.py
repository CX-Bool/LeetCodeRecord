class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dif = x^y
        res=0
        while dif:
            res += dif &1
            dif >>=1
        return res