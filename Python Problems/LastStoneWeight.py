from heapq import heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heappush(heap,i*-1)
        
        while len(heap)!=0:
            if(len(heap)==1):
                return heappop(heap)*-1
            s1= heappop(heap)*-1
            s2=heappop(heap)*-1
            smash= s1-s2
            if smash!=0:
                heappush(heap,smash*-1)
            
        return 0

ans= Solution()
print(ans.lastStoneWeight([3,7,2]))