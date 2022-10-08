from typing import List


class Solution:
    def solve(self,num):
        arr=[-1 for i in range(num+1)]
        for i in range(num+1):
            self.move(i,arr)
        print(arr)
    def move(self,num,memo):
        if num==0:
            memo[0]=0
            return 0
        if num==1:
            memo[1]=1
            return 1
        if memo[num]!=-1:
            return memo[num]
        if num%2==0: 
            memo[num]= self.move(num//2,memo)
            return memo[num]
        else: 
            memo[num]= 1+ self.move(num//2,memo)
            return memo[num]
ans= Solution()
ans.solve(5)