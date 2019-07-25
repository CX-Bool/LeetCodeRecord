# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = -1e10

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxValue(root)
        return self.result

    def maxValue(self, root):
        if not root:
            return 0
        left = max(0, self.maxValue(root.left))
        right = max(0, self.maxValue(root.right))
        self.result = max((root.val + left + right), self.result)
        return max((root.val + left), (root.val + right))

