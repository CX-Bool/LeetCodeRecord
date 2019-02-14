# 执行用时: 104 ms, 在Reshape the Matrix的Python3提交中击败了96.42% 的用户
# 列表生成式比append方法效率高
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flatten = [x for raw in nums for x in raw]
        if r*c != len(flatten):
            return nums
        else:
            return [flatten[i*c:i*c+c] for i in range(r)]

# class Solution:
#     def matrixReshape(self, nums, r, c):
#         """
#         :type nums: List[List[int]]
#         :type r: int
#         :type c: int
#         :rtype: List[List[int]]
#         """
#         rows = len(nums)
#         cols = len(nums[0])
#         if rows * cols != r * c:
#             return nums
#         flat = [j for i in nums for j in i]
#         result = []
#         for i in range(r):
#             result.append(flat[i*c:(i+1)*c])
#         return result