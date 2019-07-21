'''执行用时 :
36 ms
, 在所有 Python 提交中击败了
54.75%
的用户
内存消耗 :
13.6 MB
, 在所有 Python 提交中击败了
44.51%
的用户'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        while head:
            stack.append(head)
            head = head.next
        i = len(stack) -1
        if not stack:
            return head
        while i > 0:
            stack[i].next = stack[i-1]
            i-=1
        stack[0].next = None
        return stack[-1]

        ### recursion
        # if not head or not head.next:
        #     return head
        # newHead = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return newHead
