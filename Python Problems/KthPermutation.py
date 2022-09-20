class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s=''
        while n!=0:
            s=str(n)+s
            n=n-1
        self.solve(ip=s,op='',k=k,count=0)
    def solve(self,ip,op,k,count):
        if len(ip)==0:
            return
        if count==k:
            print(op)
            return 
        op1=op
        op2=op
        op1=op1+ip[0]
        ip=ip[1:]
        count=count+1
        self.solve(ip,op1,k,count)
        count=count+1
        self.solve(ip,op2,k,count)

ans= Solution()
ans.getPermutation(9,2)