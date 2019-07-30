class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = []
        i = 1
        if n == 1:
            return 1
        while 1:
            s = i * i
            if s <= n:
                nums.append(s)
                i += 1
            else:
                break
        len_nums = len(nums)
        res = [0] * (n + 1)
        for i in range(len_nums - 1, -1, -1):
            num = nums[i]
            for j in range(1, n + 1):
                if j < num:
                    continue
                if not res[j] and (j == num or res[j - num]):
                    res[j] = 1 + res[j - num]
                elif res[j - num]:
                    res[j] = min(res[j - num] + 1, res[j])
            # print(res,num)
        return res[n]

