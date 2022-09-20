from typing import List


class Solution:
    def shipWithinDays(self, arr: List[int], k: int) -> int:
        if len(arr)<k:
            return -1
        res=-1
        start,end=self.findMaxAndSum(arr)
        while start<=end:
            mid=int((start+end)/2)
            if self.isValidScheme(arr,mid,k)==True:
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res
    def isValidScheme(self,arr,mid,k):
        days=1
        sum=0
        for i in arr:
            sum=sum+i
            if sum>mid:
                days=days+1
                sum=i
            if days>k:
                return False
        return True

    def findMaxAndSum(self,arr):
        max=0
        sum=0
        for i in arr:
            if i>max:
                max=i
            sum=sum+i
        return max,sum


ans= Solution()
print(ans.shipWithinDays([3,2,2,4,1,4],  3))