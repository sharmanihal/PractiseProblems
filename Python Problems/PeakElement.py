from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        mid=-1
        if len(nums)==1:
            return 0
        while start<=end:
            mid=int((start+end)/2)
            if mid!=0 and mid!=len(nums)-1:
                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                    return mid
                elif nums[mid-1]>nums[mid]:
                    end=mid-1
                elif nums[mid+1]>nums[mid]:
                    start= mid+1
            else:
                if mid==0 and nums[0]>nums[1]:
                    return 0
                elif mid==0 and nums[0]<nums[1]:
                    return 1
                if mid==len(nums)-1 and nums[len(nums)-1]>nums[len(nums)-2]:
                    return len(nums)-1
                elif mid==len(nums)-1 and nums[len(nums)-1]<nums[len(nums)-2]:
                    return nums[len(nums)-2]