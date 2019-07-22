class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        m=len(matrix)
        n=len(matrix[0])
        i=j=0
        flag='d'
        for _ in range(m*n):
            res.append(matrix[i][j])
            matrix[i][j]=0
            if flag=='d':
                j+=1
                if j == n or not matrix[i][j]:
                    flag='s'
                    j-=1
                    i+=1
            elif flag=='s':
                i+=1
                if i == m or not matrix[i][j]:
                    flag='a'
                    i-=1
                    j-=1
            elif flag=='a':
                j-=1
                if j < 0 or not matrix[i][j]:
                    flag='w'
                    j+=1
                    i-=1
            elif flag=='w':
                i-=1
                if i < 0 or not matrix[i][j]:
                    flag='d'
                    i+=1
                    j+=1
        return res