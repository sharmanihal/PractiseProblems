from typing import List



class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for i in ops:
            if i.lstrip('-').replace('.', '', 1).isdigit():
                stack.append(i)
            elif i=='C':
                stack.pop()
            elif i=='D':
                num=2*int(stack[len(stack)-1]);
                stack.append(num)
            elif i=='+':
                num=int(stack[len(stack)-1])+int(stack[len(stack)-2]);
                stack.append(num)
        
        score=0
        for num in stack:
            score+=int(num);
        return score

ans= Solution()
print(ans.calPoints(["5","-2","4","C","D","9","+","+"]))