from heapq import heappop, heappush

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heap=[]
        max=-1
        for i in nums:
            if i>0:
                heappush(heap,i)
                if i>max:
                    max=i
        steps=0
        sub=0
        while max!=0:
            temp=heappop(heap)-sub
            while temp==0:
                temp=heappop(heap)-sub
            max=max-temp
            sub=sub+temp
            steps=steps+1
        return steps

ans = Solution()
print(ans.minimumOperations([58,88,77]))