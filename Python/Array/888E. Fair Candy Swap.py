# Time Limit Exceed
class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dif = int((sum(A) - sum(B)) / 2)
        for a in A:
            for b in B:
                if a-b == dif:
                    return [a, b]


if __name__ == '__main__':
    s=Solution()
    s.fairCandySwap([1,1],[2,2])