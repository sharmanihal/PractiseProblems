from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        count=0
        while i<len(nums) and j<len(nums):
            if k==0:
                count+=1
                if nums[i]%2!=0:
                    k=k+1
                i=i+1
            else:
                if nums[j]%2!=0:
                    k-=1
                j=j+1
        return count
ans= Solution()
print(ans.numberOfSubarrays([1,1,2,1,1],3))