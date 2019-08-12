# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        h=head
        l=0
        while h:
            l+=1
            h=h.next
        i = l-n
        h=head
        p=None
        while i:
            i-=1
            p=h
            h=h.next
        if not p:
            return h.next
        if not h.next:
            p.next=None
        else:p.next=h.next
        return head