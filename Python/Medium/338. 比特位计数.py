class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if not num:
            return [0]
        res = [0, 1]
        for i in range(2, num + 1):
            s = i >> 1
            r = (i & 1) + res[s]
            # print(i,s,r,i&1,res[s])
            res.append(r)
        return res
