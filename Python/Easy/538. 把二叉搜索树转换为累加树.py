# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def sumtree(root, sum_from_father):
            if not root:
                return 0
            raw_v = root.val
            raw_right_value = sumtree(root.right, sum_from_father)
            root.val += sum_from_father + raw_right_value
            raw_left_value = sumtree(root.left, root.val)
            return raw_v + raw_right_value + raw_left_value

        sumtree(root, 0)
        return root


