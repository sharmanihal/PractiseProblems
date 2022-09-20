from heapq import heappop, heappush
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap=[]
        for i in amount:
            if i!=0:
                heappush(heap,i*-1)
        seconds=0
        while len(heap)!=0:
            if len(heap)>=2:
                seconds=seconds+1
                t1= heappop(heap)*-1
                t2= heappop(heap)*-1
                t1=t1-1
                t2=t2-1
                if t1!=0:
                    heappush(heap,t1*-1)
                if t2!=0:
                    heappush(heap,t2*-1)
            elif len(heap)==1:
                seconds=seconds+heappop(heap)*-1
        return seconds

            

ans= Solution()
print(ans.fillCups([5,0,0]))