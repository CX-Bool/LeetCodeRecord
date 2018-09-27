# Accepted
class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dif = int((sum(A) - sum(B)) / 2)
        dict_a = {a:True for a in A}
        lst_a = [a for a in dict_a.keys()]
        lst_b = [a-dif for a in lst_a]
        dict_b = {b:True for b in B}
        for b in lst_b:
            if dict_b.get(b):
                return[b+dif,b]



if __name__ == '__main__':
    s=Solution()
    s.fairCandySwap([1,1],[2,2])