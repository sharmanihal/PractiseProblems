from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start=0
        end= len(nums)-1
        mid=-1
        while start<=end:
            if start==end:
                return end
            mid=int((start+end)/2)
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return mid
            if nums[mid]==nums[mid-1] and (mid-1)%2!=0:
                end=mid
                continue
            if nums[mid]==nums[mid+1] and (mid+1)%2!=0:
                start=mid
                continue
            if nums[mid]!=nums[mid-1] and (mid-1)%2==0:
                end= mid-1
                continue
            if nums[mid]!=nums[mid+1] and (mid+1)%2==0:
                start= mid+1
                continue

ans=Solution()
print(ans.singleNonDuplicate([1,3,3,4,4,8,8]))