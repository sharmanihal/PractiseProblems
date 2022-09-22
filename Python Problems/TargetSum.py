from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target= abs(target)
        sum=0
        for i in nums:
            sum=sum+i
        if (target > sum or (target+sum)%2==1):
            return 0
        subsetSum1= (sum+target)//2
        return self.countSubsetSum(nums,subsetSum1,len(nums))
        
    def countSubsetSum(self,arr,sum,n):
        dp=[[-1 for y in range(sum+1)]for x in range(n+1)]
        for i in range(n+1):
            for j in range(sum+1):
                if i==0:
                    dp[i][j]=0
                if j==0:
                    dp[i][j]=1

        for i in range(1,n+1):
            for j in range(sum+1):
                if arr[i-1]<=j:
                    dp[i][j]= dp[i-1][j-arr[i-1]] + dp[i-1][j]
                else:
                    dp[i][j]= dp[i-1][j]
        return dp[n][sum]
