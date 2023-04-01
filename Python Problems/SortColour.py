from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colourcount={}
        for num in nums:
            if num in colourcount:
                colourcount[num]=colourcount[num]+1
            else:
                colourcount[num]=1
        i=0
        colours=[0,1,2]
        for color in colours:
            if color in colourcount:
                while colourcount[color]!=0:
                    nums[i]=color
                    colourcount[color]=colourcount[color]-1
                    i=i+1
            
ans = Solution()
ans.sortColors([2,0,2,1,1,0])
        