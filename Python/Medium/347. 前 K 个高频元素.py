class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        p=[]
        for ik,iv in count.items():
            heapq.heappush(p,(-iv,ik))
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(p)[1])
        return res