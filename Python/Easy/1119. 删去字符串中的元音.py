class Solution:
    def removeVowels(self, S: str) -> str:
        res = []
        for s in S:
            if s not in 'aeiou':
                res.append(s)
        return ''.join(res)