class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        res=[[''],['()']]
        for i in range(2,n+1):
            res_i=[]
            for p,q in zip(range(i), range(i-1,-1,-1)):
                inside = res[p]
                outside = res[q]
                for instr in inside:
                    for outstr in outside:
                        # print('res{}: p:{}:{} q:{}:{}'.format(i,p,instr,q,outstr))
                        res_i.append('('+instr+')'+outstr)
            res.append(res_i)
        return res[n]