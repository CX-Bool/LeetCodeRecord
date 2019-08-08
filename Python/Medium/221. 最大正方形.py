from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        maxl = 0
        for r in range(0,m):
            for c in range(0,n):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c],dp[r+1][c],dp[r][c+1])+1
                    maxl = max(maxl,dp[r+1][c+1])
        return maxl ** 2

