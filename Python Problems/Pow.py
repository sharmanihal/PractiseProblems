class Solution:
    def __init__(self):
        self.dp = {}
    def solve(self,x,n):
        res=self.myPow(x,abs(n))    
        if n<0:
            return 1/res
        else:
            return res
    def myPow(self, x: float, n: int ) -> float:
        if x==0 :
            return 0
        if n==0:
            return 1
        if n==1:
            return x
        if self.dp.get((x,n)):
            return self.dp.get((x,n))
        if n%2==0 and n>=4:
            self.dp[(x,n)]=self.myPow(x,n//4)*self.myPow(x,n//4)*self.myPow(x,n//4)*self.myPow(x,n//4)
            return self.dp[(x,n)]
        elif n%2!=0 and n>=4:
            self.dp[(x,n)]=self.myPow(x,n//4)*self.myPow(x,n//4)*self.myPow(x,n//4)*self.myPow(x,n//4)*x
            return self.dp[(x,n)]
        elif n%2==0 and n<4:
            self.dp[(x,n)]=self.myPow(x,n//2)*self.myPow(x,n//2)
            return self.dp[(x,n)]
        elif n%2!=0 and n<4:
            self.dp[(x,n)]=self.myPow(x,n//2)*self.myPow(x,n//2)*x
            return self.dp[(x,n)]

ans= Solution()
print(ans.solve(2,10))


        
    
        