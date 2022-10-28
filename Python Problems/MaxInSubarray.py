import sys
from typing import List


#Kadane's Algoritm
class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        res=max(arr)
        currMax=1
        currMin=1
        for n in arr:
            if n==0:
                currMax=1
                currMin=1
                continue
            temp=currMax
            currMax=max(n*currMax,n*currMin,n)
            currMin=min(n*temp,n*currMin,n)
            res=max(res,currMax)
        return res
ans= Solution()
print(ans.max( [3,-1,4]))