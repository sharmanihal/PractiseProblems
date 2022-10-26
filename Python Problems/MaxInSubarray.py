import sys


class Solution:
    def max(self,arr):
        if len(arr)==2:
            return max(arr[0]*arr[1], arr[1], arr[0])
        return self.solve(arr,1)
    def solve(self,arr,product):
        if len(arr)==0:
            return product
        res1= self.solve(arr[0:len(arr)-1],product*arr[len(arr)-1])
        res2= self.solve(arr[0:len(arr)-1],arr[len(arr)-1])
        return max (res1,res2)
ans= Solution()
print(ans.max( [3,-1,4]))