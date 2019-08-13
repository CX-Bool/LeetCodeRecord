class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq
        count_items={}
        for i in words:
            count_items[i]=count_items.get(i,0)+1
        p=[]
        for ik,iv in count_items.items():
                heapq.heappush(p,(-iv,ik))
        res=[]
        #print(p)
        for _ in range(k):
            res.append(heapq.heappop(p)[1])
        return res