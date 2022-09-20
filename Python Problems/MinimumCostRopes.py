from heapq import heapify, heappop, heappush


class Solution:
    def minCost(self,arr,n) :
        heapify(arr)
        cost=0
        while len(arr)!=1:
            e1= heappop(arr)
            e2=heappop(arr)
            cost=cost+e1+e2
            heappush(arr,e1+e2)
        return cost
        
ans=Solution()
ans.minCost([4,3,2,6],4)