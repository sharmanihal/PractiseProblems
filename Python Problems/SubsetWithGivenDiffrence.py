class Solution:
    def countSubsetWithDiff(self,nums,n,diff):
        sum=0
        for i in nums:
            sum=sum+i
        subsetSum1= (sum+diff)//2
        return self.countSubsetSum(nums,subsetSum1,n)

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
ans= Solution()
print(ans.countSubsetWithDiff([7,9,3,8,0,2,4,8,3,9],10,0))