from heapq import heappop, heappush
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap=[]
        for i in nums:
            heappush(heap,i)
            if len(heap)>2:
                heappop(heap)
        return (heap[0]-1)*(heap[1]-1)
ans = Solution()
print(ans.maxProduct([3,4,5,2]))
            