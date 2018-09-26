#Accepted
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_con = 0
        cur_con = 0
        pre = 0
        for i in nums:
            if i != pre:
                max_con = max(max_con, cur_con)
                if i == 1:
                    cur_con = 1
                else:
                    cur_con = 0
            elif i == 1:
                cur_con += 1
            pre = i
        max_con = max(max_con, cur_con)
        return max_con