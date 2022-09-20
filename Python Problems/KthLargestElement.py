from heapq import heappop, heappush
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in nums:
            heappush(heap,i)
            if len(heap)>k:
                print(heappop(heap))
                
        return heappop(heap)
ans=Solution()
print(ans.findKthLargest([3,2,1,5,6,4],k=2))