from turtle import st


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        stack.append(s[0])
        for ch in s[1:]:
            if len(stack)!=0 and stack[len(stack)-1]==ch:
                stack.pop()
            else:
                stack.append(ch)
        str=''
        for i in stack:
            str+=i
        return str;
ans= Solution()
print(ans.removeDuplicates('abbaca'))