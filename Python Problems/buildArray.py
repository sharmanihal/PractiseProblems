from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        temp=nums[0]
        for i in range(len(nums)):
            if nums[i]<i:
                other=nums[i]
                nums[i]=temp
                temp=other

            else:
                temp=nums[i]
                nums[i]=nums[nums[i]]
        return nums


        

ans = Solution()
print(ans.buildArray([3,2,1,0]))
# Input: nums = [5,0,1,2,3,4]
# Output: [4,5,0,1,2,3]