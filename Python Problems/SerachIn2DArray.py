from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        j=len(matrix[0])-1
        while i<=len(matrix)-1 and j>=0:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]>target:
                j=j-1
                
            if matrix[i][j]<target:
                i=i+1
                
        return False

ans= Solution()
print(ans.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))