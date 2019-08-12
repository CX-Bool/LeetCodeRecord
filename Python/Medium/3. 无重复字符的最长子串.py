class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        dic = {}
        n = len(s)
        i = 0
        j = 0
        res = 0
        while j < n:
            if s[j] not in dic:
                dic[s[j]] = j
                j += 1
            else:
                # print(i,j)
                res = max(res, j - i)
                ni = dic[s[j]] + 1
                for ti in range(i, ni):
                    dic.pop(s[ti])
                i = ni
                dic[s[j]] = j
                j += 1
        res = max(res, j - i)
        return res

