# 执行用时: 44 ms, 在Pascal's Triangle II的Python3提交中击败了92.00% 的用户
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        result = [1,1]
        while rowIndex > 1:
            temp = [1]
            for i in range(len(result)-1):
                temp.append(result[i]+result[i+1])
            temp.append(1)
            result = temp
            rowIndex -= 1
        return result