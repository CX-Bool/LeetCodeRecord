'''执行用时 :
32 ms
, 在所有 Python 提交中击败了
68.13%
的用户
内存消耗 :
11.7 MB
, 在所有 Python 提交中击败了
35.99%
的用户'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        tail = head
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        tail.next = l1 if l1 else l2
        return head.next

