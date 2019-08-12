class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1
        res = [-1]*(amount+1)
        res[0]=0
        coins.sort()
        coins.reverse()
        for i in coins:
            for j in range(i,amount+1):
                if res[j-i] != -1:
                    if res[j] != -1:
                        res[j]=min(res[j], res[j-i]+1)
                    else:
                        res[j]=res[j-i]+1
        return res[amount]