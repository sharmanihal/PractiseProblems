from heapq import heappop, heappush
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap=[]
        for i in range(len(score)):
            heappush(heap,(score[i]*-1,i))
        arr=[]
        for i in range(len(heap)):
            pop=heappop(heap)
            print(pop)
            print(score)
            if i==0:
                score[pop[1]]="Gold Medal"
                continue
            if i==1:
                score[pop[1]]="Silver Medal"
                continue
            if i==2:
                score[pop[1]]="Bronze Medal"
                continue
            score[pop[1]]=i+1
        return score    
            
            


ans=Solution()
ans.findRelativeRanks([5,4,3,2,6])