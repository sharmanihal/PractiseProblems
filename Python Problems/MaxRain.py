from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        water=0
        while i<j:
            ind=j-i
            minimun=min(height[i],height[j])
            water=max(water,minimun*ind)
            if height[i]>height[j]:
                j=j-1
            elif height[i]<height[j]:
                i=i+1
            else:
                if height[i+1]>height[j-1]:
                    i=i+1
                else:
                    j=j-1
        print(water)
ans= Solution()
ans.maxArea([1,8,6,2,5,4,8,3,7])
