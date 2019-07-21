# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        jinwei=0
        res =ListNode(0)
        cur = res
        v=0
        while l1 and l2:
            s = l1.val+l2.val+jinwei
            if s>9:
                v=s-10
                jinwei=1
            else:
                v=s
                jinwei=0
            cur.next=ListNode(v)
            cur=cur.next
            l1=l1.next
            l2=l2.next
        l = l1 if l1 else l2
        while l:
            s = l.val+jinwei
            if s>9:
                v=s-10
                jinwei=1
            else:
                v=s
                jinwei=0
            cur.next=ListNode(v)
            cur=cur.next
            l=l.next
        if jinwei:
            cur.next=ListNode(1)
        return res.next