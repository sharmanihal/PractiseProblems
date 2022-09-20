from typing import List


class Solution:
    def nearlySorted(self, nums: List[int],target) -> int:
        start=0
        end= len(nums)-1
        mid=-1
        while start<=end:
            mid=int((start+end)/2)
            if nums[mid]==target:
                return mid
            if mid>0 and nums[mid-1]==target:
                return mid-1
            if mid<len(nums)-1 and nums[mid+1]==target:
                return mid+1
            if nums[mid]>target:
                end=mid-2
            else:
                start=mid+2
    
        return -1

ans=Solution()
print(ans.nearlySorted([3, 4, 20, 50, 80, 70],50))