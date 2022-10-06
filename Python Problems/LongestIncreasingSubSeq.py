from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums1=[]
        nums1.extend(nums)
        nums1= [*set(nums1)]
        nums1.sort()
        return self.solve(nums,nums1)
        bisect_left
    def solve(self,x,y):
        arr=[[-1 for i in range(len(y)+1)]for j in range(len(x)+1)]
        for j in range(len(y)+1):
            arr[0][j]=0
        for i in range(len(x)+1):
            arr[i][0]=0
        for i in range(1,len(x)+1):
            for j in range(1,len(y)+1):
                if x[i-1]==y[j-1]:
                    arr[i][j]=1+arr[i-1][j-1]
                else:
                    arr[i][j]=max(arr[i-1][j],arr[i][j-1])
        print(arr)
        return arr[len(x)][len(y)]
ans=Solution()
print(ans.lengthOfLIS([-1,-2,-3,-4,-5,-6]))