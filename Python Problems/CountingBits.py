class Solution:
    #If we see the arr till num=10
    # arr= [0,1,2,3,4,5,6,7,8,9,10]
    # nums=[0,1,1,2,1,2,2,3,1,2,2]
    #we can see that nums=10 no. of 1's equal to nums=5 1's and nums=5 1's is nums=2 +1
    #and nums=2 is nums=1 

    def countBits(self,num):
        arr=[- 1 for i in range(num+1)]
        for i in range(num+1):
           self.solve(i,arr)
        return arr
    def solve(self,num,memo):
        if num==0:
            memo[0]=0
            return 0
        if num==1:
            memo[1]=1
            return 1
        if memo[num]!=-1:
            return memo[num]
        
        if num%2==0:
            memo[num]=self.solve(num//2,memo)
            return memo[num]
        else:
            memo[num]=self.solve(num//2,memo)+1
            return memo[num]


ans= Solution()
print(ans.countBits(5))
