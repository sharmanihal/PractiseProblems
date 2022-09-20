from heapq import heappop, heappush
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        for i in matrix:
            for j in i:
                heappush(heap,j*-1)
                if len(heap)>k:
                    heappop(heap)
        return heappop(heap)*-1
ans=Solution()
print(ans.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))