from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[-1 for i in range(len(nums)+1)]
        memo[0]=0
        memo[1]=nums[0]
        for i in range(2,len(nums)+1):
            memo[i]=max(nums[i-1]+memo[i-2],memo[i-1])
        return memo[len(nums)]

ans= Solution()
print(ans.rob([2,7,9,3,1]))