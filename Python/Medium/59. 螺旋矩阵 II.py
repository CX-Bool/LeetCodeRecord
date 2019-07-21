'''执行用时 :
20 ms
, 在所有 Python 提交中击败了
91.77%
的用户
内存消耗 :
11.6 MB
, 在所有 Python 提交中击败了
35.79%
的用户'''
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n) ]
        i=j=0
        flag='d'
        for v in range(1,n**2+1):
            res[i][j]=v
            if flag=='d':
                j+=1
                if j == n or res[i][j]:
                    flag='s'
                    j -= 1
                    i += 1
            elif flag=='s':
                i+=1
                if i == n or res[i][j]:
                    flag='a'
                    i -= 1
                    j -= 1
            elif flag=='a':
                j-=1
                if j<0 or res[i][j]:
                    flag='w'
                    j += 1
                    i -= 1
            elif flag=='w':
                i-=1
                if i<0 or res[i][j]:
                    flag='d'
                    i+=1
                    j+=1
        return res