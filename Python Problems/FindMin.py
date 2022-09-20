from tkinter import N
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        mid=-1
        n= len(nums)
        while start<=end:
            mid=int((start+end)/2)
            if nums[start]<=nums[end]:
                return nums[start]
            next=(mid+1)%n
            prev=(mid+n-1)%n
            if nums[mid]<nums[next] and nums[mid]<=nums[prev]:
                return nums[mid]
            if nums[mid]<=nums[end]:
                end=mid-1
            if nums[mid]>=nums[start]:
                start=mid+1
ans=Solution()
print(ans.findMin([3,4,5,1,2]))