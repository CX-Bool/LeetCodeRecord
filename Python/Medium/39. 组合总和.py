class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if candidates:
            candidates.sort()
        n = len(candidates)

        def find(lst, tar, pre):
            if not tar:
                return [pre]
            res = []
            n = len(lst)
            for i in range(n - 1, -1, -1):
                x = lst[i]
                # print(x,tar,lst,pre,pre[-1])

                if pre and pre[-1] < x:  # 去重精髓
                    continue
                if x == tar:
                    res.append(pre + [x])
                if x < tar:
                    res += find(lst, tar - x, pre + [x])
            return res

        for i in range(n - 1, -1, -1):
            x = candidates[i]
            pre = []
            if x <= target:
                res += find(candidates, target - x, pre + [x])
            candidates.pop()
        return res
