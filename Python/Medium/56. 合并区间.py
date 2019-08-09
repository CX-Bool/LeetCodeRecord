from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        left,right = intervals[0]
        res = []
        for x in intervals:
            if right >= x[0]:
                right = max(right,x[1])
            else:
                res.append([left,right])
                left,right=x
        else:
            res.append([left,right])
        return res

# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         while (root != None):
#             if root.left != None:
#                 most_right = root.left
#                 while most_right.right != None: most_right = most_right.right
#                 most_right.right = root.right
#                 root.right = root.left
#                 root.left = None
#             root = root.right
#         return
