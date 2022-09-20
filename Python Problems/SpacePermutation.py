class Solution:
    arr=[]
    def spacePermute(self,ip:str,op:str)->str:
        if len(ip)==0:
            self.arr.append(op)
            return
        op1=op
        op2=op
        op1=op1+ip[0]
        op2=op2+'_'+ip[0]
        ip=ip[1:]
        self.spacePermute(ip,op1)
        self.spacePermute(ip,op2)
        return self.arr
        


ans= Solution()
print(ans.spacePermute('n',''))