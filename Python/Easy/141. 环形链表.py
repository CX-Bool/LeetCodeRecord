'''执行用时 :
52 ms
, 在所有 Python 提交中击败了
69.90%
的用户
内存消耗 :
18.7 MB
, 在所有 Python 提交中击败了
5.13%
的用户'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = set()
        while head:
            if head in nodes:
                return True
            nodes.add(head)
            head = head.next
        return False
        ### 快慢指针
        # if not head or not head.next:
        #     return False
        # slow = head
        # fast = head.next
        # while slow != fast:
        #     if not fast or not fast.next:
        #         return False
        #     slow = slow.next
        #     fast = fast.next.next
        # else:
        #     return True
