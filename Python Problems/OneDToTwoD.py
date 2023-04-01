from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n*m !=len(original):
            return []
        newArr=[]
        i=0
        curr=n
        while m!=0:
            arr=[]
            while i!=curr:
                arr.append(original[i])
                i=i+1
            newArr.append(arr)
            m=m-1
            curr=curr+n
        return newArr
                
            
ans= Solution()
ans.construct2DArray([1,2,3,4],2,2)