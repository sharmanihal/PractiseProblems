from heapq import heappop, heappush
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        for i in range(len(nums)):
            heappush(heap,(nums[i],i))
            if len(heap)>k:
                heappop(heap)
        num=[]
        heap2=[]
        for i in heap:
            heappush(heap2,(i[1],i[0]))
        print(heap2)
        for i in range(len(heap2)):
            num.append(heappop(heap2)[1])
        return num
ans= Solution()
print(ans.maxSubsequence([-1,-2,3,4],3))
        
