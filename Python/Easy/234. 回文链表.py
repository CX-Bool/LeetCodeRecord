# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # res=[]
        # while head:
        #     res.append(head.val)
        #     head=head.next
        # return res == res[::-1]
        if not head or not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = rev
            rev = temp

        slow = slow.next if fast else slow
        # print(rev)
        # print(slow)
        # print(fast)
        while rev and slow:
            if rev.val != slow.val:
                return False
            rev = rev.next
            slow = slow.next
        return True