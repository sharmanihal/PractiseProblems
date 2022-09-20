from tkinter.tix import Tree
from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        deleted=False
        score=0
        temp=nums[0]
        i=0
        while 1:
            deleted=False
            i=0
            while i<=len(nums)-1:
                if  i>=1 and i<len(nums) and temp>nums[i]:
                    deleted=True
                    temp=nums[i]
                    nums=nums[:i] + nums[i+1 :]
                    i=i-1
                elif i>=1 and i<len(nums) and temp<=nums[i]:
                    temp=nums[i]
                i=i+1
            print(str(score)+" score",nums, i)
            if deleted==False:
                break
            score=score+1
            
            temp=nums[0]
        return score       

ans= Solution()
print(str(ans.totalSteps([7,11,1]))+"score")
# Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
