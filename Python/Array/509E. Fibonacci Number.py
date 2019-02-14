# 执行用时: 40 ms, 在Fibonacci Number的Python3提交中击败了100.00% 的用户
class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        fs = [0,1]
        for i in range(2,31):
            fs.append(fs[i-2]+fs[i-1])
        return fs[N]