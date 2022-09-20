from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n=0
        for i in expression:
            if not i.isdigit():
                n=n+1
        n=n-1
        self.solve(open=n-1,close=n,op='(')

    def solve(self,open,close,op):
        if open==0 and close==0:
            print(op)
            return
        if close<open:
            return
        op1=op
        op2=op
        if open!=0:
            op1=op1+'('
            self.solve(open-1,close,op1)
        if close!=0:
            op2=op2+')'
            self.solve(open,close-1,op2)
        return
ans=Solution()
ans.diffWaysToCompute('2-1-1')