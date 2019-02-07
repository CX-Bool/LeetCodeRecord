class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A = list(map(abs, A))
        A.sort()
        A = list(map(lambda a: a ** 2, A))
        return A

# 执行用时: 208 ms, 在Squares of a Sorted Array的Python3提交中击败了56.00% 的用户