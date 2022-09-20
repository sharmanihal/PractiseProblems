class Solution:
    def fib(self, n: int,dict={}) -> int:
        if n==1:
            return 1
        if n==0:
            return 0
        if dict.get(n)!=None:
            return dict[n]

        val=self.fib(n-1)+self.fib(n-2)
        dict[n]=val
        return val
ans=Solution()
print(ans.fib(30))