# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        num = 0
        while fast:
            if not fast.next:
                return None
            num += 1
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        fast = head
        for _ in range(num):
            fast = fast.next
        slow = head
        while fast and slow:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next