# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        r_root = root

        def reverse_tree(root):
            if not root:
                return None
            new_root = TreeNode(root.val)
            new_root.left, new_root.right = reverse_tree(root.right), reverse_tree(root.left)
            return new_root

        r_root = reverse_tree(r_root)

        # def dfs(root):
        #     if root:
        #         dfs(root.left)
        #         print(root.val)
        #         dfs(root.right)
        # dfs(root)
        # dfs(r_root)

        def compare(root, r_root):
            # print(root, r_root)
            if not root and not r_root:
                return True
            if (not root and r_root) or (not r_root and root):
                return False
            if root.val != r_root.val:
                return False
            return compare(root.left, r_root.left) and compare(root.right, r_root.right)

        return compare(root, r_root)