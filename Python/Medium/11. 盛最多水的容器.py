'''
执行用时 :
140 ms
, 在所有 Python 提交中击败了
59.57%
的用户
内存消耗 :
13.1 MB
, 在所有 Python 提交中击败了
18.12%
的用户
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        area = min(height[0], height[-1]) * (j - i)
        while i < j:

            temp_area = min(height[i], height[j]) * (j - i)
            area = max(area, temp_area)
            # print('%s, %s, %s, %s'%(area, temp_area, i, j))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area