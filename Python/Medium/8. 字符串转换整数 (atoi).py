class Solution(object):
    def myAtoi(self, strs):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        first = True
        start = end = 0
        for i in range(len(strs)):
            # print(i)
            if first and strs[i] == ' ':
                continue
            if first and strs[i] in '+-0123456789':
                first = False
                start = i
            elif strs[i] in '0123456789':
                continue
            else:
                end = i
                break
        else:
            end = None
        # print(list(strs))
        res = strs[start:end]
        # print(res,start,end)
        if not res:
            return 0
        try:
            res = int(res)
        except:
            return 0
        if res < -2 ** 31:
            res = -2 ** 31
        elif res >= 2 ** 31:
            res = 2 ** 31 - 1
        return res
