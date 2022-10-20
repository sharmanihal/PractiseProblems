from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo1=[-1 for i in range(len(nums)-1)]
        memo2=[-1 for i in range(len(nums)-1)]
        res1= self.solve(nums[0:len(nums)-1],len(nums)-2,memo1)
        res2= self.solve(nums[1:],len(nums)-2,memo2)
        return max(res1,res2)
    def solve(self,nums,n,memo):
        if n<0:
            return 0
        if memo[n]!=-1:
            return memo[n]
        memo[n]= max(nums[n]+self.solve(nums,n-2,memo),self.solve(nums,n-1,memo))
        return memo[n]
ans= Solution()
print(ans.rob([1,2,3,1]))