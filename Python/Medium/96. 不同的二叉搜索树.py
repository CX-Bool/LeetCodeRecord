class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp_sub = [[0 for _ in range(x + 1)] for x in range(n + 1)]

        dp[0] = 1
        dp_sub[0][0] = 1
        for i in range(1, n + 1):
            s = 0
            for j in range(1, i + 1):
                if not dp_sub[i][j]:
                    dp_sub[i][j] = dp[j - 1] * dp[i - j]
                s += dp_sub[i][j]
            dp[i] = s
            # print(dp)
        # print(dp)
        # print(dp_sub)
        return dp[n]