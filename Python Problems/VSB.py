from textwrap import indent


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0;
        stack=[];
        index=0
        var=""
        for str in s:
            if(str=='('):
                count=count+1;
                var=var.__add__('(')
            if(str==')'):
                var=var.__add__(')')
                count=count-1
            if(count==0):
                stack.append(var)
                var=''
                index=index+1
        var=''
        for s in stack:
           var= var.__add__((s[1:len(s)-1]))
        return var;

ans= Solution()
print(ans.removeOuterParentheses("(()())(())(()(()))"))