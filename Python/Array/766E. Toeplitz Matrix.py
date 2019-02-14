# 执行用时: 56 ms, 在Toeplitz Matrix的Python3提交中击败了99.52% 的用户
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row_num = len(matrix)
        for i in range(row_num - 1):
            a = matrix[i][:-1]
            b = matrix[i+1][1:]
            if a != b:
                return False
        return True