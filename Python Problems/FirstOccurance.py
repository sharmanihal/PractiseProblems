from typing import List


class Solution:
    def firstOccrance(self, arr: List[int],target) -> int:
        start=0
        end=len(arr)-1
        mid=-1
        save=-1
        while start<=end:
            mid=int((start+end)/2)
            if arr[mid]==target:
                save=mid
                end=mid-1
                #to get last occurance just do start=mid+1
            if arr[mid]>target:
                end=mid-1
            if arr[mid]<target:
                start=mid+1
        print(save)


ans= Solution()
ans.firstOccrance([1,1,2,2,3,3,4,5,6,7,8],8)