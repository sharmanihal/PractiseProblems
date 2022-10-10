from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [1,1]
        elif numRows==0:
            return [1]
        return self.solve(numRows)
    def solve(self,numRows):
        if numRows==0:
            return [1]
        if numRows==1:
            return [1,1]
        arr=self.solve(numRows-1)
        i=0
        j=1
        nums=[1]
        while j<len(arr):
            nums.append(arr[i]+arr[j])
            i=i+1
            j=j+1
        nums.append(1)
        return nums

ans= Solution()
print(ans.generate(2))
            
            