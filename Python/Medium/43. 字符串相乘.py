class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # return str(int(num1)*int(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        num1 = [int(c) for c in num1]
        num2 = [int(c) for c in num2]

        l1 = len(num1)
        l2 = len(num2)
        res = [0 for _ in range(l1 + l2)]
        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                res[i + j] += n1 * n2
        for i in range(l1 + l2 - 1):
            if res[i] > 9:
                res[i + 1] += res[i] // 10
                res[i] %= 10
        res = [str(x) for x in res]
        while res[-1] == '0' and len(res) > 1:
            res.pop()
        return ''.join(res)[::-1]