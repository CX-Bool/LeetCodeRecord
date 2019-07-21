'''执行用时 :
28 ms
, 在所有 Python 提交中击败了
67.62%
的用户
内存消耗 :
11.6 MB
, 在所有 Python 提交中击败了
34.35%
的用户'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n and n % 2 ==0:
            n/=2
        return n==1