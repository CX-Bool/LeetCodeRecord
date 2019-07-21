# manacher算法
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list(s)
        new_s = '@#'+'#'.join(slist)+'#$'
        p = [0 for _ in range(len(new_s))]
        old_i=max_right=0
        for i in range(1,len(new_s)-1):
            if(i<max_right):
                p[i]=min(p[2*old_i-i], max_right-i)
            else:
                p[i]=1
            while new_s[i-p[i]]==new_s[i+p[i]]:
                p[i]+=1
        l=max(p)
        index=p.index(l)
        ss =  new_s[index-l+1:index+l]
        return ''.join(ss.split('#'))