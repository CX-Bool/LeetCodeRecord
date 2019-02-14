# 执行用时: 360 ms, 在Sum of Even Numbers After Queries的Python3提交中击败了5.26% 的用户
class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        even = [x for x in A if x % 2 == 0]
        s = sum(even)
        result = []
        for q in queries:
            i = q[1]
            old = A[i]
            A[i] += q[0]
            if old % 2 == 0:
                s -= old
            if A[i] % 2 == 0:
                s += A[i]
            result.append(s)
        return result