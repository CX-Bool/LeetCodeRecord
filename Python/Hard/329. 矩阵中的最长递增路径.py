class Solution:
    rec = None
    ans = 0
    m = n = 0
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    mat = None

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.mat = matrix
        self.rec = [[0 for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.ans = max(self.ans, self.bfs(i, j))
        # print(self.rec)
        return self.ans + 1

    def bfs(self, i, j):
        if not self.rec[i][j]:
            for dx, dy in self.direction:
                ni, nj = i + dx, j + dy
                if 0 <= ni < self.m and 0 <= nj < self.n and self.mat[ni][nj] > self.mat[i][j]:
                    self.rec[i][j] = max(self.rec[i][j], 1 + self.bfs(ni, nj))
        return self.rec[i][j]
