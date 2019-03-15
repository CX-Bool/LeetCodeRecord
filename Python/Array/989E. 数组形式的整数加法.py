# 执行用时 : 340 ms, 在Add to Array-Form of Integer的Python3提交中击败了41.67% 的用户
# 内存消耗 : 13.2 MB, 在Add to Array-Form of Integer的Python3提交中击败了100.00% 的用户
class Solution:
    def addToArrayForm(self, A: list[int], K: int) -> list[int]:
        i = -1
        j = 0
        while K:
            if i < -len(A):
                A.insert(0,0)
            A[i] += K %10
            K = K // 10
            i -= 1
            j += 1
        i = -1
        n = -len(A)
        while i>-j or (A[i] > 9 and i>n):
            if A[i] > 9:
                A[i] -= 10
                A[i-1] += 1
            i -= 1
        if A[0] > 9:
            A[0] -= 10
            A.insert(0,1)
        return A
