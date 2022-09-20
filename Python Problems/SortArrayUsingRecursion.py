from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return
        else :
            ele= nums.pop()
            self.sortArray(nums)
            self.insert(nums,ele)
            return nums
    def insert(self,nums: List[int],ele):
        if len(nums)==0 or nums[len(nums)-1]>=ele:
            nums.append(ele)
            return
        else :
            val= nums[len(nums)-1]
            nums.pop()
            self.insert(nums,ele)
            nums.append(val)
ans= Solution()
print(ans.sortArray([1,5,0,2]))

        