from typing import List


##Memoization 
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        memo1=[-1 for i in range(len(nums))]
        memo2=[-1 for i in range(len(nums))]
        res1= self.solve(nums[0:len(nums)-1],memo1)
        res2= self.solve(nums[1:],memo2)
        return max(res1, res2)
    def solve(self,nums,memo):
        memo[0]=0
        memo[1]=nums[0]
        for i in range(2, len(memo)):
            memo[i]= max(nums[i-1]+memo[i-2],memo[i-1])
        return memo[len(memo)-1]
    
ans= Solution()
print(ans.rob([1,2,3,1]))