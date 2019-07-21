# 执行用时 : 108 ms, 在Find Common Characters的Python3提交中击败了100.00% 的用户
# 内存消耗 : 13 MB, 在Find Common Characters的Python3提交中击败了100.00% 的用户
class Solution:
    def commonChars(self, A: list[str]) -> list[str]:
        len_strs = len(A)
        import string
        dic = {'%s'%char : [0]*len_strs for char in string.ascii_lowercase}
        for i, s in enumerate(A):
            for c in s:
                dic[c][i] += 1
        res = []
        for k, v in dic.items():
            num = min(min(v),(sum(v) // len_strs))
            while num >0:
                res.append(k)
                num -= 1
        return res