'''执行用时 :
28 ms
, 在所有 Python 提交中击败了
98.03%
的用户
内存消耗 :
14.6 MB
, 在所有 Python 提交中击败了
29.55%
的用户'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
