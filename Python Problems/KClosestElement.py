from heapq import heappush
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        for i in range(len(arr)-1):
            if abs(arr[i] - x) < abs(arr[i+1] - x) or (abs(arr[i] - x) == abs(arr[i+1] - x) and arr[i] < arr[i+1]):
                print(arr[i])
            else:
                print(arr[i+1])


ans=Solution()
ans.findClosestElements([1,2,3,4,5],4,3)