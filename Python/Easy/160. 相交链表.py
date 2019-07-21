"""
执行用时 :
220 ms
, 在所有 Python 提交中击败了
95.68%
的用户
内存消耗 :
41.9 MB
, 在所有 Python 提交中击败了
14.98%
的用户
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def length(head):
            h = head
            count = 0
            while h:
                h=h.next
                count += 1
            return count
        la = length(headA)
        lb = length(headB)
        longhead, shorthead, longlen, shortlen= (headA, headB, la, lb) if la > lb else (headB, headA, lb, la)
        delta = longlen - shortlen
        for _ in range(delta):
            longhead = longhead.next
        for _ in range(shortlen):
            if not longhead and not shorhead:
                return None
            if longhead == shorthead:
                return longhead
            else:
                longhead = longhead.next
                shorthead = shorthead.next
        return None

