'''
13.1 MB
, 在所有 Python 提交中击败了
7.49%
的用户'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.split()
        reslist = [x[::-1] for x in slist]
        return ' '.join(reslist)
