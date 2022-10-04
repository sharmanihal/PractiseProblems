class Solution:
    def __init__(self) -> None:
        self.local=0
        self.max=0
    def lcString(self,x:str,y:str):
        self.solve(x,y)
        return self.max
    def solve(self,x:str,y:str)->int:
        if len(x)==0 or len(y)==0:
            return 0
        if x[len(x)-1]==y[len(y)-1]:
            self.local=self.local+1
            return self.solve(x[0:len(x)-1],y[0:len(y)-1])
        else:
            if self.local>self.max:
                self.max=self.local
            self.local=0
            return self.solve(x[0:len(x)-1],y[0:len(y)-1])
ans= Solution()
print(ans.lcString('aobtcel','awbicel'))
