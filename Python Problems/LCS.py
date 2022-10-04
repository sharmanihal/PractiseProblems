class Solution:
     def lsc(self,x,y,xn,yn):
        max=0
        arr=[[-1 for i in range(yn+1)]for j in range(xn+1)]
        for j in range(yn+1):
            arr[0][j]=0
        for i in range(xn+1):
            arr[i][0]=0
        for i in range(1,xn+1):
            for j in range(1,yn+1):
                if x[i-1]==y[j-1]:
                    arr[i][j]= 1+ arr[i-1][j-1]
                else:
                    arr[i][j]= 0
                if arr[i][j]>max:
                    max=arr[i][j]
        return max
ans= Solution()
print(ans.lsc('abcde','abce',len('abcde'),len('abfc')))