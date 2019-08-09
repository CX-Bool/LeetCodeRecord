class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T: return []
        n = len(T)
        tail=[(T[-1],n-1)]
        res=[0]
        for i in range(n-2, -1, -1):
            m=60000
            for j in range(len(tail)):
                tj,ij=tail[j]
                if T[i]<tj:
                    m=min(m,ij-i)
                    #print(T[i],tj,i,ij,ij-i,m)
                elif T[i]==tj:
                    tail[j]=(T[i],i)
                    break
                else:
                    tail.insert(j,(T[i],i))
                    break
            else:
                tail.append((T[i],i))
            if m==60000: m=0
            res.append(m)
        res.reverse()
        #print(tail)
        return res