from heapq import heappop, heappush


class Solution:
    def largestInteger(self, num: int) -> int:
        evenHeap=[]
        oddHeap=[]
        digits = [int(x) for x in str(num)]
        for i in digits:
            if i %2==0:
                heappush(evenHeap,i*-1)
            else:
                heappush(oddHeap,i*-1)
        max=''
        for i in digits:
            if i%2==0:  
                temp=heappop(evenHeap)*-1
                max+=str(temp)
            else:
                temp=(heappop(oddHeap)*-1)
                max+=str(temp)
        return int(max)

ans= Solution()
print(ans.largestInteger(65875))