from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        duplicate= list(nums)
        duplicate.sort()
        i,j=0,len(duplicate)-1
        while i<len(duplicate) and j>=0:
            if duplicate[i]+duplicate[j]>target:
                j=j-1
            elif duplicate[i]+duplicate[j]<target:
                i=i+1
            else :
                break
        counter=0
        finalI,finalJ=-1,-1
        k=0
        while k<len(nums):
            if nums[k]==duplicate[i] and counter==0:
                counter=counter+1
                finalI=k
            if nums[k]==duplicate[j]:
                finalJ=k
            k=k+1
        return [finalI,finalJ]
ans=Solution()
print(ans.twoSum(nums = [3,3], target = 6))