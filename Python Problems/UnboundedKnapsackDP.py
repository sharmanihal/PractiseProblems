from typing import List


class Solution:
    def __init__(self,n,capacity) -> None:
        self.arr=[[-1 for y in range(capacity+1)]for x in range(n+1)]
        
    def unbounded(self,wt:List[int],val:List[int],capacity,n):
        if capacity<=0 or n<=0:
            return 0
        if self.arr[n][capacity]!=-1:
            return self.arr[n][capacity]
        if wt[n-1]>capacity:
            self.arr[n][capacity]= self.unbounded(wt,val,capacity,n-1)
            return self.arr[n][capacity]
        if wt[n-1]<= capacity:
            self.arr[n][capacity]= max(val[n-1]+self.unbounded(wt,val,capacity-wt[n-1],n),(self.unbounded(wt,val,capacity,n-1)))
            return self.arr[n][capacity]
    

ans = Solution(3,100)
print(ans.unbounded(wt = [5, 10, 15],val = [10, 30, 20],capacity= 100,n=3))

