# Accepted
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        raw_num = len(matrix)
        for i in range(raw_num - 1):
            a = matrix[i][:-1]
            b = matrix[i+1][1:]
            if a != b:
                return False
        return True