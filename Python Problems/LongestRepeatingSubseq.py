class Solution:
    def lrs(self,x)->int:
        return self.solve(x,x)[::-1]
    def solve(self,x,y):
        arr=[["" for i in range(len(y)+1)]for j in range(len(x)+1)]
        for i in range(1,len(x)+1):
            for j in range(1,len(y)+1):
                if x[i-1]==y[j-1] and i!=j:
                    arr[i][j]=x[i-1]+arr[i-1][j-1]
                else:
                    s1= arr[i-1][j]
                    s2=arr[i][j-1]
                    if len(s1)>len(s2):
                        arr[i][j]=s1
                    else:
                        arr[i][j]=s2
        return (arr[len(x)][len(y)])
ans= Solution()
print(ans.lrs('letsleetcode'))
