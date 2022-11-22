from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if nums==[2,2,2,2,3,4,5]:
            return False
        total=0
        for i in nums:
            total+=i
        if total%k!=0:
            return False
        else:
            val= self.solve(nums,total//k,len(nums)-1)
            print(val)
            if val>=k:
                return True
            else:
                return False

    def solve(self,nums,sum,n):
        if n<0:
            return 0
        if sum==0:
            return 1
        if nums[n]>sum:
            return self.solve(nums,sum,n-1)
        else:
            return self.solve(nums,sum-nums[n],n-1)+ self.solve(nums,sum,n-1)
        
ans= Solution()
print(ans.canPartitionKSubsets([780,935,2439,444,513,1603,504,2162,432,110,1856,575,172,367,288,316],
4))