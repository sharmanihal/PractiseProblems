import re
from typing import List



class Solution:
    def __init__(self) -> None:
        self.globalMax= -sys.maxsize - 1
    def maxSubArray(self, nums: List[int]) :
        flag=True
        localMax= -sys.maxsize - 1
        for i in nums:
            if i>localMax: localMax=i
            if i>=0:
                flag=False
                break
        if flag: localMax
        res=self.solve(nums,len(nums)-1)
        return max(self.globalMax,res,localMax)
    def solve(self,nums,n):
        if n==0:
            return nums[0]
        result= max(nums[n]+self.solve(nums,n-1),nums[n])
        if self.globalMax<result:
            self.globalMax=result
        return result
ans= Solution()
print(ans.maxSubArray([1,-1,-2]))
print(ans.maxsu)