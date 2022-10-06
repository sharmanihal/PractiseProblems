

class Solution:
    def minDel(self,s)->int:
        return len(s)-self.lcs(s,s[::-1])
    def lcs(self,x,y)->int:
        arr=[[-1 for i in range(len(y)+1)]for j in range(len(x)+1)]
        for j in range(len(y)+1):
            arr[0][j]=0
        for i in range(len(x)+1):
            arr[i][0]=0
        for i in range(1,len(x)+1):
            for j in range(len(y)+1):
                if x[i-1]==y[j-1]:
                    arr[i][j]=1+arr[i-1][j-1]
                else:
                    arr[i][j]=max(arr[i-1][j],arr[i][j-1])
        return arr[len(x)][len(y)]
ans= Solution()
print(ans.minDel('agbcba'))

