# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # check=[]
        # h = head
        # while h :
        #     check.append(h.val)
        #     h =h.next
        # print(check)
        if not head:
            return
        elif not head.next:
            return head
        elif not head.next.next:
            if head.val < head.next.val:
                return head
            else:
                res = head.next
                head.next = None
                res.next = head
                return res

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(fast)

        res = newhead = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                newhead.next = l1
                newhead = newhead.next
                l1 = l1.next
            else:
                newhead.next = l2
                newhead = newhead.next
                l2 = l2.next
        newhead.next = l1 if l1 else l2
        return res.next

