from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal=-1
        vector=[]
        for i in range(len(arr)-1,-1,-1):
            if i==len(arr)-1:
                vector.append(maxVal)
                maxVal=arr[i]
            else :
                vector.append(maxVal)
                if arr[i]>maxVal:
                    maxVal=arr[i]
        vector.reverse()
        print(vector)
            
        

ans= Solution()
ans.replaceElements([17,18,5,4,6,1])
# Output: [18,6,6,6,1,-1]