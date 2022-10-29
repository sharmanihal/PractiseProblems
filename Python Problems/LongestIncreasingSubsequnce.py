import sys
from typing import List

class Solution: 
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub=[]
        for ele in nums:
            if len(sub)==0:
                sub.append(ele)
            else:
                if ele>sub[len(sub)-1]:
                    sub.append(ele)
                else:
                    index= self.findPos(sub,ele)
                    sub[index]=ele
        return len(sub)
    #This fucntion is used to find a index of element in arr such that
    #element should be smallest element such that it is >= num
    def findPos(self,arr,num)->int:
        low=0
        hi=len(arr)
        while low < hi:
            mid = (low + hi) // 2
            if arr[mid] < num:
                low = mid + 1
            else:
                hi = mid
        return low








ans= Solution()
ans.lengthOfLIS([10,9,2,5,3,7,101,18])
    #     num=sys.maxsize
    #     return self.solve(nums,num,len(nums))
    # def solve(self,nums,num,n):
    #     if n==0:
    #         return 0
        
    #     if num>nums[n-1]:
    #         res1= 1+self.solve(nums,nums[n-1],n-1)
    #         res2=self.solve(nums,num,n-1)
    #         return max(res1,res2)
    #     else:
    #         res1= self.solve(nums,num,n-1)
    #         res2=self.solve(nums,num,n-1)
    #         return max(res1,res2)

