# Accepted
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        raw_num = len(A)
        col_num = len(A[0])
        res = []
        for i in range(col_num):
            new_raw = []
            for j in range(raw_num):
                new_raw.append(A[j][i])
            res.append(new_raw)
        return res