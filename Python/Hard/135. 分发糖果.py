class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        res=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                res[i]=res[i-1]+1
        # if ratings[-1]>ratings[0]:
        #     res[-1]=res[0]+1
        #     print(res)
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                res[i]=max((res[i+1]+1),res[i])
        # print(res)
        return sum(res)