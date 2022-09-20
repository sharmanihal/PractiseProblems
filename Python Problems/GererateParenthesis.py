class Solution:
    def __init__(self) -> None:
        self.arr=[]
    def generateParanthesis(self,n)->list:
        return self.validParenthesis(n-1,n,'(')

    def validParenthesis(self,open,close,op):
        if open==0 and close==0:
            self.arr.append(op)
            return
        if close<open:
            return
        op1=op
        op2=op
        if open!=0:
            op1+='('
            self.validParenthesis(open-1,close,op1)
        if close!=0:
            op2+=')'
            self.validParenthesis(open,close-1,op2)
        return self.arr




ans= Solution()
print(ans.generateParanthesis(3))