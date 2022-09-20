from math import ceil
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        end= self.findMax(nums)
        start=0
        res=-1
        mid=-1
        while start<=end:
            mid=int((start+end)/2)
            if  mid!=0 and  self.isValidScheme(nums,mid,threshold)==True:
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res
    def isValidScheme(self,nums,mid,threshold):
        sum=0
        for i in nums:
            sum=sum+ ceil(i/mid)
            if sum>threshold:
                return False
        return True
    def findMax(self,nums):
        max=-1
        for i in nums:
            if i >max:
                max=i
        return max
ans= Solution()
print(ans.smallestDivisor([21212,10101,12121],1000000))