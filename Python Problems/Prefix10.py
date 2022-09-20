class Solution:
    def __init__(self) -> None:
        self.arr=[]
    def prefix(self,n):
        return self.findBinary(1,0,n-1,'1')
    def findBinary(self,one,zero,n,op):
        if zero>one:
            return
        if n==0:
            self.arr.append(op)
            return self.arr
        op1=op
        op2=op
        op1=op1+'0'
        self.findBinary(one,zero+1,n-1,op1)
        op2=op2+'1'
        self.findBinary(one+1,zero,n-1,op2)
        return self.arr

ans= Solution()
print(ans.prefix(3))
        
        


