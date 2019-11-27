# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue=[]
        level=0
        res=[]
        if not root: return []
        queue.append((root,0))
        while queue:
            r,lv=queue.pop(0)
            if lv == len(res):
                res.append([])
            res[lv].append(r.val)
            if r.left:
                queue.append((r.left,lv+1))
            if r.right:
                queue.append((r.right,lv+1))
        return res