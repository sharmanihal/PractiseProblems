from typing import List


import operator
ops = { "+": operator.add, "-": operator.sub ,"*":operator.mul}
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res=[]
        for i in range(len(expression)):
            if expression[i]=='*' or expression[i]=='+' or expression[i]=='-':
                a=self.diffWaysToCompute(expression[0:i])
                b=self.diffWaysToCompute(expression[i+1:])
                print(a,b,expression[i])
                for  x in a :
                    for y in b:
                        if expression[i] == '-': 
                            res.append(int(x) - int(y))
                        elif expression[i]  == '+': 
                            res.append(int(x) + int(y))
                        elif expression[i]  == '*':
                            res.append(int(x) * int(y))
        if len(res)==0:
            res.append(int(expression))
            
        return res
ans= Solution()
print(ans.diffWaysToCompute("2*3-4*5"))