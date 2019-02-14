# 执行用时: 40 ms, 在Pascal's Triangle的Python3提交中击败了100.00% 的用户
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1],[1,1]]
        for i in range(3,numRows+1):
            temp = [1]
            a = result[i-2]
            b = a[1:]
            for j in range(len(b)):
                temp.append(a[j]+b[j])
            temp.append(1)
            result.append(temp)
        return result