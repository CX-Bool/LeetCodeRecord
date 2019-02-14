# 执行用时: 172 ms, 在Sort Array By Parity II的Python3提交中击败了83.10% 的用户
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        i = 0
        l = len(A)
        j = l - 1
        while l > 0:
            while A[i] % 2 != 0:
                i += 1
            result.append(A[i])
            i += 1
            while A[j] % 2 != 1:
                j -= 1
            result.append(A[j])
            j -= 1
            l -= 2
        return result