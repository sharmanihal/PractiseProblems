from heapq import heappop, heappush
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for i in nums:
            if map.get(i)==None:
                map[i]=1
            else:
                map[i]=map[i]+1
        heap=[]
        for i in map:
            heappush(heap,(map[i]*-1,i))
        arr=[]
        while k!=0:
            arr.append(heappop(heap)[1])
            k=k-1
        return (arr)
ans=Solution()
ans.topKFrequent([1,1,1,1,2,2,2],2)