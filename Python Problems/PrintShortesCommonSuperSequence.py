class Solution:
    def scs(self,x,y)->str:
        return self.solve(x,y)
    def solve(self,x,y):
        arr=[[-1 for i in range(len(y)+1)]for j in range(len(x)+1)]
        for j in range(len(y)+1):
            arr[0][j]=0
        for i in range(len(x)+1):
            arr[i][0]=0
        for i in range(1,len(x)+1):
            for j in range(1,len(y)+1):
                if x[i-1]==y[j-1]:
                    arr[i][j]= 1+arr[i-1][j-1]
                else:
                    arr[i][j]=max(arr[i-1][j], arr[i][j-1])
        i= len(x)
        j=len(y)
        s=""
        while i>0 and j>0:
            if x[i-1]==y[j-1]:
                s=x[i-1]+s
                j=j-1
                i=i-1
            else:
                if arr[i-1][j]>arr[i][j-1]:
                    s=x[i-1]+s
                    i=i-1
                elif arr[i-1][j]<arr[i][j-1]:
                    s=y[j-1]+s
                    j=j-1
        while i>0:
            s=x[i]+s
            i=i-1
        while j>0:
            s=y[j]+s
            j=j-1
        return s


ans= Solution()
print(ans.scs('acbcf','abcdaf'))