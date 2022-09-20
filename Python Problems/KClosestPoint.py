from heapq import heappop, heappush
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # √(x1 - x2)2 + (y1 - y2)2).
        heap=[]
        for i in points:
            heappush(heap,(i[0]**2+i[1]**2,i))
        arr=[]
        while k!=0:
            arr.append(heappop(heap)[1])
            k=k-1
        return arr
ans=Solution()
ans.kClosest([[3,3],[5,-1],[-2,4]],2)