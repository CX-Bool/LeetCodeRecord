# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def merge(r1,r2):
            if not r1 and not r2:
                return None
            elif not r1 and r2:
                return r2
            elif r1 and not r2:
                return r1
            else:
                head=TreeNode(r1.val+r2.val)
                head.left=merge(r1.left,r2.left)
                head.right=merge(r1.right,r2.right)
                return head
        return merge(t1,t2)