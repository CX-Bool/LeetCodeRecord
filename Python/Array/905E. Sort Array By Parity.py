# Accepted
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        even = []
        odd = []
        for x in A:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)
        return even + odd


# from collections import deque
#
# class Solution:
#     def sortArrayByParity(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         arr = deque()
#         for num in A:
#             if(num % 2 == 0):
#                 arr.appendleft(num)
#             else:
#                 arr.append(num)
#         return list(arr)