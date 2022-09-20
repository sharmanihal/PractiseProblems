class Solution:
    def josephus(self,n,k)->int:
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        self.solve(arr,k-1,0)
    def solve(self,arr,k,index):
        if len(arr)==1:
            print(arr[0])
            return
        next= (index+k)%len(arr)
        del arr[next]
        self.solve(arr,k,next)
        return

ans= Solution()
ans.josephus(40,7)