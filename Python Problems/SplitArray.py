from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start=0
        end= len(nums)-1
        res=-1
        mid=-1
        while start<=end:
            mid=int((start+end)/2)
            if self.isValidScheme(nums,m,mid)==True:
                res=mid
                end=mid-1
            else:
                start=mid+1

    def isValidScheme(self,nums,m,mid):



    # def findSum(self,nums):
    #     sum=0
    #     for i in nums:
    #         sum=sum+i
    #     return sum
ans= Solution()
ans.splitArray(nums = [7,2,5,10,8], m = 2)