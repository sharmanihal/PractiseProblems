from typing import List


class Solution:
    def contigiousProduct(self,nums:List[int],prod,n):
        if n==len(nums)-1:
            return nums[n]
        x= self.contigiousProduct(nums,nums[n]*prod,n+1)
        y=self.contigiousProduct(nums,prod,n+1)
        return max(x,y,prod)


ans= Solution()
print(ans.contigiousProduct([9, -6, 10, 3] ,1,0))