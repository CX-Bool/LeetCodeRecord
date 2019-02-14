# 执行用时: 56 ms, 在Flipping an Image的Python3提交中击败了99.36% 的用户
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for row in A:
            result.append([1 - col for col in row[::-1]])
        return result