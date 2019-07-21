'''执行用时 :
44 ms
, 在所有 Python 提交中击败了
13.48%
的用户
内存消耗 :
11.6 MB
, 在所有 Python 提交中击败了
38.25%
的用户'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        smin = strs[0]
        for s in strs:
            if len(s) < len(smin):
                smin = s
        res = 0
        num = 0
        quit = False
        for i in range(len(smin)):
            for j in range(len(strs)):
                if strs[j][i] != smin[i]:
                    quit = True
                    break
            if quit:
                break
            num += 1
        return smin[:num]
