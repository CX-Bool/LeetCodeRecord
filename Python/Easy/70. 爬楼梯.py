class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1, 1]
        if n < 2:
            return 1
        else:
            for i in range(2, n + 1):
                res.append(res[-1] + res[-2])
        return res[-1]

