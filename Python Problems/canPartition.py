from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=0
        for i in nums:
            total+=i
        if total%2!=0:
            return False
        else:
            arr=[[-1 for i in range(len(nums)) ]for j in range(total//2+1)]
            return self.solve(nums,total//2,len(nums)-1,arr)
    def solve(self,nums,sum,n,arr):
        if n<0:
            return False
        if sum==0:
            return True
        if arr[sum][n]!=-1:
            return arr[sum][n]
        if nums[n]>sum:
            arr[sum][n]= self.solve(nums,sum,n-1,arr)
            return arr[sum][n]
        else:
            arr[sum][n]= self.solve(nums,sum-nums[n],n-1,arr) or self.solve(nums,sum,n-1,arr)
            return arr[sum][n]
ans= Solution()
print(ans.canPartition([1,5,11,5]))

