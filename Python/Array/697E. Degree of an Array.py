# 执行用时: 108 ms, 在Degree of an Array的Python3提交中击败了66.67% 的用户
# 内存消耗: 8.2 MB, 在Degree of an Array的Python3提交中击败了94.29% 的用户
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        start = {}
        end = {}
        for i, num in enumerate(nums):
            if count.get(num):
                count[num] += 1
                end[num] = i
            else:
                count[num] = 1
                start[num] = i
                end[num] = i
        find = {}
        maxv = -1
        for k, v in count.items():
            maxv = max(maxv, v)
            if find.get(v):
                find[v].append(k)
            else:
                find[v] = [k]
        index = find[maxv][0]
        degree = end[index] - start[index] + 1
        for num in find[maxv]:
            degree = min(degree, (end[num] - start[num] + 1))
        return degree
