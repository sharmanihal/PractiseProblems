from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start,end= self.findSumMax(piles,h)
        mid=-1
        res=-1
        while start<=end:
            mid=int((start+end)/2)
            if self.isValidScheme(piles,h,mid)==True:
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res

    def isValidScheme(self,piles,h,mid):
        hours=0
        for i in piles:
            if i<=mid:
                hours=hours+1
            if i>mid:
                hours= hours+ceil(i/mid)
            if hours>h:
                return False
        return True
       
    def findSumMax(self,piles,h):
        max=-1
        sum=0
        for i in piles:
            sum=sum+i
            if max<i:
                max=i
        return ceil(sum/h),max
ans= Solution()
print(ans.minEatingSpeed(piles = [3,6,7,11], h = 8))