from typing import List
import sys
from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i,j=0,0
        arr = deque([])  
        vector=[]
        while j<len(nums) and i<len(nums):
            arr=self.removeAllSmallerThan(nums[j],arr)
            if j-i+1<k:
                j+=1
            else:
                vector.append(arr[0])
                if arr[0]==nums[i]:
                    arr.popleft()
                i=i+1
                j=j+1
        return vector
    def removeAllSmallerThan(self,num,arr:deque)->deque:
        i=len(arr)-1
        while i>=0:
            if arr[i]<num:
                arr.pop()
                i=i-1
            else:
                break
        arr.append(num)
        return arr
ans= Solution()
print(ans.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))

        