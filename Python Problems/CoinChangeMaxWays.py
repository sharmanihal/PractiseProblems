class Solution:
    def coinChange(self,coin,sum):
        print(self.subsetSum(coin,sum,len(coin)))
    def subsetSum(self,nums,sum,n):
        arr=[[-1 for y in range(sum+1)]for x in range(n+1)]
        for j in range(sum+1):
                arr[0][j]=0
        for i in range(n+1):
                arr[i][0]=1
        for i in range(1,n+1):
            for j in range(sum+1):
                if nums[i-1]<=j:
                    arr[i][j]= arr[i][j-nums[i-1]]+ arr[i-1][j]
                else:
                    arr[i][j]=arr[i-1][j]
        return arr[n][sum]

ans= Solution()
ans.coinChange([1,2,5],5)