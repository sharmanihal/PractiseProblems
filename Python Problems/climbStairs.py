class Solution:

    def climbStairs(self,n:int)->int:
        n1=1
        n2=2
        j=2
        while j!=n:
            temp=n1+n2
            n1=n2
            n2=temp
            j=j+1
        return  n2

ans= Solution()
ans.climbStairs(6)