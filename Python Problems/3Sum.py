from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        i=0
        ans=[]
        while i<len(nums):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                i=i+1
                continue
            low,high=i+1,len(nums)-1
            
            sum=0
            while low<high:
                sum= nums[i]+nums[low]+nums[high]
                if sum>0:
                    high=high-1
                elif sum<0:
                    low=low+1
                else:
                    ans.append([nums[i],nums[low],nums[high]])

                    #This is to eleminate the duplicate triplets buy skipping the duplicate numbers altogether
                    last_low_occurence = nums[low]
                    last_high_occurence = nums[high];  
                    while low < high and nums[low] == last_low_occurence:
                        low=low+1
                    
                    while low < high and nums[high] == last_high_occurence:
                        high=high-1
            i=i+1
        return ans
                    
                    
ans = Solution()
ans.threeSum([-1,0,1,2,-1,-4])