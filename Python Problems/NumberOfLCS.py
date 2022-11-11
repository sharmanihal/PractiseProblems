
from typing import List


class Solution: 
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
class Solution: 
    def findNumberOfLIS(self, nums: List[int]) -> int:
        sub=[]
        for ele in nums:
            if len(sub)==0:
                sub.append(ele)
            else:
                if ele>sub[len(sub)-1]:
                    sub.append(ele)
                else:
                    index= self.findPos(sub,ele)
                    sub[index]=ele
        return len(sub)
    def findPos(self,arr,num)->int:
        low=0
        hi=len(arr)
        while low < hi:
            mid = (low + hi) // 2
            if arr[mid] < num:
                low = mid + 1
            else:
                hi = mid
        return low
ans = Solution()
print(ans.findNumberOfLIS([2,2,2,2,2]))