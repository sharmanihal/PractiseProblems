from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[-1]*(target+1)
        return self.subsetSum(nums,target,dp,len(nums))
    def subsetSum(self,nums,target,dp,n):
        if target==0:
            return 1
        if target<0 or n==0:
            return 0
        if dp[target]!=-1:
            return dp[target]
        if nums[n-1]<=target:
            dp[target]= self.subsetSum(nums,target-nums[n-1],dp,len(nums))+ self.subsetSum(nums,target,dp,n-1)
            return dp[target]
             
        else:
            dp[target]=self.subsetSum(nums,target,dp,n-1)
            return dp[target]
ans= Solution()
print(ans.combinationSum4(nums = [1,2,3], target = 4))