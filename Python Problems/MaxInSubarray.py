import sys


class Solution:
    def max(self,arr):
        return self.solve(arr,1)
    def solve(self,arr,product):
        if len(arr)==0:
            return product
        return max(self.solve(arr[0:len(arr)-1],product*arr[len(arr)-1]),self.solve(arr[0:len(arr)-1],1))
    
ans= Solution()
print(ans.max( [-2,0,-1]))