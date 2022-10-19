##Dynamic Programming approach
from inspect import trace
from typing import List
'''
The basic idea behin this solution is that we need to find two subsets s1 and s2 such that there 
diffrence is equal to the given sum.

s1 will be subset of all positive numbers i.e the numbers to which we will add +
s2 will be subset of all negative numbers i.e the numbers to which we will add -

e.g
[1,1,2,3] sum =1

s1= [+1,+3]
s2=[-1,-2]

sub both s1 and s2 = 1


s1+s2= total sum
s1-s2= target sum

Add both equation we get 
    2 * S1= target sum + Total Sum
    S1= (target sum + Total Sum)/2
    So S1= (1 + 7)/2=4
So we need to count such subsets whose sum is 4.

'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=0
        for i in nums:
            total=total+i
        if target>total or (target+total)%2==1:
            return 0
        sum=(total+target)//2
        return self.countSubset(nums,sum,len(nums))
    def countSubset(self,arr,sum,n):
        dp=[[-1 for i in range(sum+1)]for j in range(n+1)]
        for i in range(n+1):
            for j in range(sum+1):
                if i==0:
                    dp[i][j]=0
                if j==0:
                    dp[i][j]=1
        for i in range(1,n+1):
            for j in range(sum+1):
                if arr[i-1]>j:
                    #if the item > sum then we ingore the item
                    dp[i][j]=dp[i-1][j]
                else:
                    #if the item is = or less than sum then eiter take it or leave it
                    dp[i][j]=dp[i-1][j-arr[i-1]] + dp[i-1][j]
        return dp[n][sum]
ans=Solution()
print(ans.findTargetSumWays([1,1,2,3],1))