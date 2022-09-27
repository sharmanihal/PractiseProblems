from cmath import inf
import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans=self.solve(coins,amount,len(coins))
        if  ans==sys.maxsize -1:
            return -1
        else:
            return ans
    def solve(self,nums,sum,n):
        dp=[[-1 for y in range(sum+1)]for x in range(n+1)]
        for i in range(n+1):
                dp[i][0]=0
        for j in range(sum+1):
                dp[0][j]=sys.maxsize-1
        for i in range(1,n+1):
            for j in range(1,sum+1):
                if nums[i-1]<=j:
                    dp[i][j]= min(1+dp[i][j-nums[i-1]], dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][sum]
ans= Solution()
print(ans.coinChange([1,2,5],11))