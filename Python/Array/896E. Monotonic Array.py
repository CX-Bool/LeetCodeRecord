# 执行用时: 112 ms, 在Monotonic Array的Python3提交中击败了96.58% 的用户
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n < 2:
            return True
        k = 0
        while A[k] == A[k+1]:
            k += 1
            if k == n-1:
                return True
        flag = A[k+1]>A[k]
        for i in range(k+1,n-1):
            if A[i+1]==A[i]:
                continue
            if (A[i+1]>A[i]) != flag:
                return False
        return True

# 执行用时: 152 ms, 在Monotonic Array的Python3提交中击败了64.51% 的用户
# class Solution:
#     def isMonotonic(self, A):
#         """
#         :type A: List[int]
#         :rtype: bool
#         """
#         if not A:
#             return False
#         increase = decrease = True
#         pre = A[0]
#         for i in A:
#             if i > pre:
#                 decrease = False
#             elif i < pre:
#                 increase = False
#             pre = i
#             if not increase and not decrease:
#                 return False
#         else:
#             return True