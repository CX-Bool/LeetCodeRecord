# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.find_depth(root)
        return self.res

    def find_depth(self, root):
        if not root:
            return 0
        l = self.find_depth(root.left)
        r = self.find_depth(root.right)
        self.res = max(self.res, l + r)
        return 1 + max(l, r)
