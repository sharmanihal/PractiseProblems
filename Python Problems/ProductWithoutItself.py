from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        freq=0
        mul=1
        for i in nums:
            if i==0:
                freq=freq+1
            else:
                mul=mul*i
        arr=[0 for x in range(len(nums))]
        j=0
        while j<len(nums):
            if nums[j]==0:
                freq=freq-1
                if freq==0:
                    arr[j]=mul
                else:
                    arr[j]=0
                freq=freq+1
            else:
                if freq!=0:
                    arr[j]=0
                else:
                    arr[j]=mul/nums[j]
            j=j+1
        print(arr)
ans= Solution()
ans.productExceptSelf(nums = [-1,1,0,-3,3])