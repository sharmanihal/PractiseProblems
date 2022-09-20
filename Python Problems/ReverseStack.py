class Solution :
    def reverseStack(self,stack) :
	
	# stack is a python list here
        if len(stack)==1:
            return stack 
        val= stack.pop()
        self.reverseStack(stack)
        self.insert(stack,val)
        return stack
    def insert(self,stack,ele):
        if len(stack)==0:
            stack.append(ele)
        else:
            val= stack.pop()
            self.insert(stack,ele)
            stack.append(val)
ans= Solution()
print(ans.reverseStack([1,2,3,4,5]))