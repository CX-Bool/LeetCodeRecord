class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        dic={}
        base=ord('a')
        def strto01(s):
            res=[0]*26
            for c in s:
                res[ord(c)-base]+=1
            res=map(str,res)
            return ''.join(res)
        for s in strs:
            s01 = strto01(s)
            if s01 not in dic:
                res.append([])
                dic[s01]=len(res)-1
            res[dic[s01]].append(s)
        return res