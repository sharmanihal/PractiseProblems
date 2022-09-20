from tkinter import N
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        mid=-1
        n=len(nums)
        min=-1
        while start<=end:
            mid=int((start+end)/2)
            if nums[start]<=nums[end]:
                min= start
                break
            next=(mid+1)%n 
            prev=(mid+n-1)%n 
            if nums[mid]<=nums[prev] and nums[mid]<=nums[next]:
                min= mid
                break
            if nums[start]<=nums[mid]:
                start=mid+1
            if nums[mid]<=nums[end]:
                end=mid-1
        start=min
        end= len(nums)-1
        mid=-1
        while start<=end:
            mid=int((start+end)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            elif nums[mid]<target:
                start=mid+1
        
        start=0
        end= min-1
        mid=-1
        while start<=end:
            mid=int((start+end)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            elif nums[mid]<target:
                start=mid+1
        return -1
        
ans= Solution()
print(ans.search([7,8,1,2,3,4,5,6],2))
            