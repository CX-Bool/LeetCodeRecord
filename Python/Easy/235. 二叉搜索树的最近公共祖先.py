'''执行用时 :
80 ms
, 在所有 Python 提交中击败了
83.13%
的用户
内存消耗 :
19.9 MB
, 在所有 Python 提交中击败了
38.59%
的用户'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        head = root
        while head.val != p.val or head.val!=q.val:
            if head.val > p.val and head.val > q.val:
                head = head.left
            elif head.val < p.val and head.val < q.val:
                head = head.right
            else:
                break
        return head