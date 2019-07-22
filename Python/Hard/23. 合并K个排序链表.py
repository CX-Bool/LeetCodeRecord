# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        res=head
        if not lists:
            return
        empty_index=[]
        for i,node in enumerate(lists):
            if not node:
                empty_index.append(i)
        if empty_index:
            empty_index=empty_index[::-1]
            for i in empty_index:
                lists.pop(i)
        while lists:
            min_val = lists[0].val
            min_i=0
            for i,node in enumerate(lists):
                if node.val<min_val:
                    min_val, min_i=node.val,i
            res.next = ListNode(min_val)
            res = res.next
            if lists[min_i].next:
                lists[min_i] = lists[min_i].next
            else:
                lists.pop(min_i)
        return head.next