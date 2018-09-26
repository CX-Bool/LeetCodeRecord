# Accepted
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

if __name__ == '__main__':
    s=Solution()
    s.isMonotonic([1,2,2,3])