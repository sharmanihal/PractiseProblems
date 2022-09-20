
from operator import le
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left=[]
        for i in range(len(height)):
            if i==0:
                left.append(height[i])
            elif left[i-1]>height[i]:
                left.append(left[i-1])
            else:
                left.append(height[i])
        rigth=[]
        for i in range(len(height)-1,-1,-1):
            if i==len(height)-1:
                rigth.append(height[i])
            elif rigth[len(height)-2-i]>height[i]:
                rigth.append(rigth[len(height)-2-i])
            else:
                rigth.append(height[i])
        rigth.reverse()
        water=0
        for i in range(len(height)):
            water=water+ (min(left[i],rigth[i])-height[i])
        return water


ans= Solution()
print(ans.trap([3,0,0,2,0,4]))