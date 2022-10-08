from typing import List


class Solution:
    def __init__(self) -> None:
        self.res=[]
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows>2:
            self.res.append([1])
            self.res.append([1,1])
        elif numRows==2:
            return [[1],[1,1]]
        elif numRows==1:
            return [1]
        self.solve(numRows)
        return self.res
    def solve(self,numRows):
        if numRows==1:
            return [1]
        if numRows==2:
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
        self.res.append(nums)
        return nums

ans= Solution()
print(ans.generate(14))
            
            