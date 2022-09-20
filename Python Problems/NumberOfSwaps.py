from math import ceil


class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        for i in s:
            if len(stack)>0 and i==']' and stack[len(stack)-1]=='['  :
                stack.pop()
            else:
                if i==']':
                    stack.append(']')
                elif i=='[':
                    stack.append('[')
        pairs= len(stack)/2;
        return ceil(pairs/2)
ans= Solution()
print(ans.minSwaps(']]][[['))