from typing import List


class Solution:
    def __init__(self):
        self.arr={}
    def letterCasePermutation(self, s: str) -> List[str]:
        return self.permuteWithCaseChange(s,'')
    def permuteWithCaseChange(self,ip:str,op:str):
        if len(ip)==0:
            if self.arr.get(op)==None:
                self.arr[op]=0
            return
        op1=op
        op2=op
        op1+=ip[0].lower()
        op2+=ip[0].upper()
        ip=ip[1:]
        self.permuteWithCaseChange(ip,op1)
        self.permuteWithCaseChange(ip,op2)
        return list(self.arr.keys())

ans= Solution()
print(ans.letterCasePermutation('a1b2'))
