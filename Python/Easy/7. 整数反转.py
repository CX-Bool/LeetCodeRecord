class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        pre=''
        if s[0]=='-':
            pre='-'
            s=s[1:]
        rs = pre+s[::-1]
        res = int(rs)
        if res > 2**31-1 or res < -2**31:
            res = 0
        return res