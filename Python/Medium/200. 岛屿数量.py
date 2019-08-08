class Solution:
    def __init__(self):
        self.root = {}

    def findRoot(self, pos):
        if self.root[pos] == pos:
            return pos
        else:
            return self.findRoot(self.root[pos])

    def union(self, pos1, pos2):
        self.root[self.findRoot(pos2)] = self.findRoot(pos1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                self.root[(i, j)] = (i, j)
        di = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # print(self.root)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for d in di:
                        dm, dn = d
                        if 0 <= i + dm < m and 0 <= j + dn < n and grid[i + dm][j + dn] == '1':
                            self.union((i, j), (i + dm, j + dn))
                else:
                    del self.root[(i, j)]
        res = 0
        for k in self.root:
            if self.findRoot(k) == k:
                res += 1
        return res