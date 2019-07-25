# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n = 0
        h = head
        if not head:
            return head
        while h:
            n += 1
            h = h.next
        k %= n
        offset = n - k
        h = head
        for _ in range(offset - 1):
            h = h.next
        r = h.next
        h.next = None
        rr = r
        if not rr:
            return head
        while rr.next:
            rr = rr.next
        rr.next = head
        return r
