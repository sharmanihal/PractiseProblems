from multiprocessing.dummy import Array


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        invalid=[]
        stack=[]
        for i in range(len(s)):
            if len(stack)==0 and s[i]==')':
                invalid.append([')',i])
                continue
            
            if s[i]=='(':
                stack.append(['(',i])
                continue;
            
            if s[i]==')' and len(stack)>0 and stack[len(stack)-1][0]=='(':
                stack.pop()
                continue
            if s[i]==')' and len(stack)>0 and stack[len(stack)-1][0]!='(':
                stack.append([')',i])
                continue
        invalid=invalid+stack
        print(invalid)
        arr=list(s)
        for i in range(len(invalid)):
            invalid[i][1]=invalid[i][1]-i
            del arr[invalid[i][1]]
        str=''
        for i in arr:
            str=str+i
        print(str)

ans=Solution()
ans.minRemoveToMakeValid("lee(t(c)o)de)))")