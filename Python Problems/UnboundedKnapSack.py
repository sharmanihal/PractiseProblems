from typing import List


class Solution:
    def unboundedKnapsack(self,wt:List[int],val:List[int],capacity,n):
        if capacity<=0 or n<=0:
            return 0
        if wt[n-1]>capacity:
            return self.unboundedKnapsack(wt,val,capacity,n-1)
        if wt[n-1]<= capacity:
            return max(val[n-1]+self.unboundedKnapsack(wt,val,capacity-wt[n-1],n),(self.unboundedKnapsack(wt,val,capacity,n-1)))


ans = Solution()
print(ans.unboundedKnapsack(wt = [5, 10, 15],val = [10, 30, 20],capacity= 100,n=3))

