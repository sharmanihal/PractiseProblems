from typing import List
import sys

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        i=0
        closest=sys.maxsize
        print(nums)
        while i<len(nums):
            low,high=i+1,len(nums)-1
            sum=0
            while low<high:
                sum= nums[i]+nums[low]+nums[high]
                if abs(sum - target) < abs(closest- target):
                    closest= sum
                if sum-target==0:
                    closest=target
                    break
                if sum>target:
                    high=high-1
                elif sum<target:
                    low=low+1
            i=i+1
        return closest
                    
                    
ans = Solution()
print(ans.threeSumClosest([1,1,1,0],100 ))