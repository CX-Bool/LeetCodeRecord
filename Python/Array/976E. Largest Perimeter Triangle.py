# 执行用时: 92 ms, 在Largest Perimeter Triangle的Python3提交中击败了99.17% 的用户
class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        while len(A)>=3:
            if A[-3]+A[-2]<=A[-1]:
                A.pop()
            else:
                return A[-3]+A[-2]+A[-1]
        return 0