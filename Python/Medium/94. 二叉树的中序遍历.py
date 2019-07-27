# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        left = self.inorderTraversal(root.left)
        mid = [root.val]
        right = self.inorderTraversal(root.right)
        return left+mid+right
# 迭代算法
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         r, stack = [], []
#         while True:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             if not stack:
#                 return r
#             node = stack.pop()
#             r.append(node.val)
#             root = node.right
#         return r
