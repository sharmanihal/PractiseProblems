from typing import List


class Solution:
    def rodCut(self,peices:List[int],price:List[int],length,n):
        arr=[[-1 for y in range(length+1) ]for x in range(n+1)]
        for i in range(n+1):
            for j in range(length+1):
                if i==0 or j==0:
                    arr[i][j]=0
        for i in range(n+1):
            for j in range(length+1):
                if peices[i-1]>j:
                    arr[i][j]= arr[i-1][j]
                elif peices[i-1]<=j:
                    arr[i][j]= max(price[i-1]+arr[i][j-peices[i-1]], arr[i-1][j])
        return arr[n][length]
ans= Solution()
print(ans.rodCut([1,2,3,4,5,6,7],[1,5,8,9,10,17,17],8,7))