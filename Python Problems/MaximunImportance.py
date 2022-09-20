from heapq import heappop, heappush
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        map={}
        for i in roads:
            for j in i:
                if map.get(j)==None:
                    map[j]=1
                else:
                    map[j]=map[j]+1
        heap=[]
        print(map)
        for i in map:
            heappush(heap,((map.get(i))*-1,i))
        arr=[0]*n
        print(heap)
        for i in range(len(heap)):
            arr[(heappop(heap)[1])]=n
            n=n-1
        max=0
        for i in roads:
            for j in i:
                max=max+ arr[j]
        return max

ans = Solution()
print(ans.maximumImportance( n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))