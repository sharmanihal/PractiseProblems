from typing import List
class Solution:

        
    def unbounded(self,wt:List[int],val:List[int],capacity,n):
        arr=[[-1 for y in range(capacity+1)]for x in range(n+1)]
        for i in range(n+1):
            for j in range(capacity+1):
                if i==0 or j==0:
                    arr[i][j]=0
        for i in range(1,n+1):
            for j in range(1,capacity+1):
                if wt[i-1]>j:
                    arr[i][j]= arr[i-1][j]
                if wt[i-1]<= j:
                    arr[i][j]= max(val[i-1]+arr[i][j-wt[i-1]],arr[i-1][j])
        return arr[n][capacity]
    

ans = Solution()
print(ans.unbounded(wt = [5, 10, 15],val = [10, 30, 20],capacity= 100,n=3))

