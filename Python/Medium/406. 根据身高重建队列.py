class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(x[0],-x[1]))
        people.reverse()
        #print(people)
        res=[]
        for p in people:
            #print(p)
            res.insert(p[1],p)
        return res