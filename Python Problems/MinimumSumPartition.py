class Solution:
    def minDifference(self, nums,n) -> int:
        sums=0
        for i in nums:
            sums=sums+i
        arr=self.subsetSum(nums,sums,len(nums))
        numArr=[]
        for i in range((len(arr)+1)//2):#range(sums//2+1)
            if arr[i]==True:
                numArr.append(i)
        return sums-2*numArr[-1]
        
    def subsetSum(self,arr,sum,n):
        dp=[ [ -1 for y in range( sum+1) ] for x in range( n+1) ]
        for i in range(n+1):
            for j in range(sum+1):
                if i==0:
                    dp[i][j]=False
                if j==0:
                    dp[i][j]=True
        for i in range(1,n+1):
            for j in range(1,sum+1):
                if arr[i-1]<=j:
                    dp[i][j]= dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]= dp[i-1][j]
        return dp[n]   
ans= Solution()
print(ans.minDifference([1,6,11,5],4))