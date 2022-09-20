from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        start=0
        end=self.findMax(bloomDay)
        res=-1
        while start<=end:
            mid=int((start+end)/2)
            if self.isValidScheme(bloomDay,mid,m,k)==True:
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res


    def isValidScheme(self,bloomDay,mid,b,f):
        boq=0
        flower=0
      
        for i in range(len(bloomDay)):
            if bloomDay[i]<=mid:
                flower=flower+1
            if bloomDay[i]>mid:
                flower=0
            if flower==f:
                boq=boq+1
                flower=0
        if boq>=b:
            return True
        else:
            return False
            

    def findMax(self,arr):
        sum=0
        for i in arr:
            sum=sum+i
        return sum
        
ans= Solution()
print(ans.minDays(   bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))