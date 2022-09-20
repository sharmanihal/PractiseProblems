from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        i=0
        j=0
        stack.append(pushed[i])
        while i<len(pushed) and j<len(popped):
            if len(stack)>0 and popped[j]==stack[len(stack)-1]:
                stack.pop()
                j=j+1
            else:
                if i+1>=len(pushed):
                    return False
                i=i+1
                stack.append(pushed[i])
        if len(stack)==0:
            return True
        else :
            return False

ans= Solution()

print(ans.validateStackSequences([1,0],  [1,0]))