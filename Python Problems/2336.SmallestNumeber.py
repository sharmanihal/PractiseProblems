from heapq import heapify, heappop, heappush
from time import sleep


class SmallestInfiniteSet:
    nums=[]
    def __init__(self):
        self.nums = list(range(1,100+1))
        heapify(self.nums)

    def popSmallest(self) -> int:
        return heappop(self.nums)
        

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            heappush(self.nums,num)


ans = SmallestInfiniteSet()
print(ans.popSmallest())
print(ans.popSmallest())
ans.addBack(3)
print(ans.popSmallest())
ans.addBack(2)
print(ans.popSmallest())
print(ans.popSmallest())


# ["SmallestInfiniteSet","popSmallest","popSmallest","addBack","popSmallest","addBack","popSmallest","popSmallest"]
# [[],[],[],[3],[],[2],[],[]]