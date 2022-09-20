from typing import List
class Solution:
    def minDiffrence(self, arr: List[int],target) -> int:
        start=0
        end=len(arr)-1
        mid=-1
        diff=100*200
        while start<=end:
            mid=int((start+end)/2)
            if abs(target-arr[mid])<diff:
                diff=abs(target-arr[mid])
            if arr[mid]<=target:
                start=mid+1
            if arr[mid]>target:
                end=mid-1
        return diff
            

ans= Solution()
print(ans.minDiffrence( arr = [1,3,8,10,15], target = 12))