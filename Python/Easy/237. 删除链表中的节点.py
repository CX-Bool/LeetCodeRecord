'''执行用时 :
28 ms
, 在所有 Python 提交中击败了
90.86%
的用户
内存消耗 :
12.3 MB
, 在所有 Python 提交中击败了
29.82%
的用户'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            node = None