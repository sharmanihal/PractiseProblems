from tabnanny import verbose
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        vector=[]
        
        for i in range(len(temperatures)-1,-1,-1):
            if len(stack)==0:
                vector.append(0);
            elif len(stack)>0 and stack[len(stack)-1][0]>temperatures[i]:
                vector.append(stack[len(stack)-1][1]-i)
            elif len(stack)>0 and stack[len(stack)-1][0]<=temperatures[i]:
                while len(stack)>0 and stack[len(stack)-1][0]<=temperatures[i]:
                    stack.pop()
                if len(stack)==0:
                    vector.append(0)
                else:
                    vector.append(stack[len(stack)-1][1]-i)
            stack.append([temperatures[i],i])
        vector.reverse()
        return vector

ans= Solution()
ans.dailyTemperatures([73,74,75,71,69,72,76,73])