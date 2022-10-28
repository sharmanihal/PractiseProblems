import sys
from typing import List


class Solution: 
    def lengthOfLIS(self, nums: List[int]) -> int:
        num=sys.maxsize
        arr=[[-1 for i in range(max(nums)+1)]for j in range(len(nums)+1)]
        return self.solve(nums,num,len(nums),arr)
    def solve(self,nums,num,n,arr):
        if n==0:
            return 0
        if num!=sys.maxsize and arr[n][num]!=-1:
            return arr[n][num]
        if num>nums[n-1]:
            res1= 1+self.solve(nums,nums[n-1],n-1,arr)
            res2=self.solve(nums,num,n-1,arr)
            if num==sys.maxsize:
                num=nums[n-1]
            arr[n][num]=max(res1,res2)
            return arr[n][num]
        else:
            res1= self.solve(nums,num,n-1,arr)
            res2=self.solve(nums,num,n-1,arr)
            arr[n][num]=max(res1,res2)
            return arr[n][num]


ans= Solution()
print(ans.lengthOfLIS([-2,-1]))