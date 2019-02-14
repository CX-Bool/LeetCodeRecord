# 执行用时: 112 ms, 在Fair Candy Swap的Python3提交中击败了43.31% 的用户
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



# 执行用时: 4424 ms, 在Fair Candy Swap的Python3提交中击败了2.64% 的用户
# class Solution:
#     def fairCandySwap(self, A, B):
#         """
#         :type A: List[int]
#         :type B: List[int]
#         :rtype: List[int]
#         """
#         dif = (sum(A)-sum(B))//2
#         for a in A:
#             if a - dif in B:
#                 return [a, a-dif]