from operator import ipow


class Solution:
    def countGoodNumbers(self,n:int)->int:
        fours=0
        fives=0
        mod=1000000007
        if n%2==0:
            fours=n//2
            fives=fours
        else:
            fours=n//2
            fives=fours+1
        return (self.ipow(4,fours,mod)*self.ipow(5,fives,mod))%mod
    def ipow(self,a,b,mod):
        if b==0:
            return 1
        x=self.ipow(a,b/2,mod)
        if b%2==0:
            return (x*x)%mod
        else:
            return (((a*x)%mod)*x)%mod

ans= Solution()
print(ans.countGoodNumbers(806166225460393))

