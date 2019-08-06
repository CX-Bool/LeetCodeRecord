class Solution:
    def __init__(self):
        self.root = []

    def findRoot(self, i):
        if self.root[i] != i:
            return self.findRoot(self.root[i])
        else:
            return i

    def union(self, i, j):
        self.root[self.findRoot(i)] = self.findRoot(j)

    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        n = len(M)
        self.root = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j]:
                    self.union(i, j)
        res = 0
        for i in range(n):
            if self.root[i] == i:
                res += 1
        return res

