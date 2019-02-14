# 执行用时: 11048 ms, 在Two Sum II - Input array is sorted的Python3提交中击败了0.95% 的用户
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i = j = 0
        while i < n:
            j = i + 1
            while j < n:
                s = numbers[i]+numbers[j]
                if s == target:
                    return i+1,j+1
                if s > target:
                    break
                j += 1
            i += 1