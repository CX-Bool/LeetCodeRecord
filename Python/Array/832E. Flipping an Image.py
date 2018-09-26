# Accepted
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for raw in A:
            new_raw = raw[::-1]
            for i in range(len(new_raw)):
                new_raw[i] = 1-new_raw[i]
            res.append(new_raw)
        return res