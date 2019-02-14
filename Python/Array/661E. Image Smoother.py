#执行用时: 660 ms, 在Image Smoother的Python3提交中击败了75.85% 的用户
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(M)
        cols = len(M[0])
        result = [[0 for _ in range(cols)] for _ in range(rows)]
        delta = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
        for r in range(rows):
            for c in range(cols):
                count = 0
                s = 0
                for dx,dy in delta:
                    if 0<=c+dx<cols and 0<= r+dy<rows:
                        count += 1
                        s += M[r+dy][c+dx]
                result[r][c] = s//count
        return result