# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    father = {}

    def findfather(self, root):
        if root.left:
            self.father[root.left] = root
            self.findfather(root.left)
        if root.right:
            self.father[root.right] = root
            self.findfather(root.right)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.father = {root: None}
        self.findfather(root)
        p_father = p
        p_depth = 0
        while p_father:
            p_depth += 1
            p_father = self.father[p_father]

        q_father = q
        q_depth = 0
        while q_father:
            q_depth += 1
            q_father = self.father[q_father]

        long_node, short_node = (p, q) if p_depth > q_depth else (q, p)
        dif = abs(p_depth - q_depth)
        for _ in range(dif):
            long_node = self.father[long_node]
        while long_node:
            if long_node == short_node:
                return long_node
            long_node = self.father[long_node]
            short_node = self.father[short_node]