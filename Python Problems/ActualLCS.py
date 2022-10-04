class Solution:

    def lcs(self,x,y):
        st= self.solve(x,y)
        st=st[::-1]
        res, i, j = "", 0, 0
        for c in st:
            while i<=len(x)-1 and x[i] != c:
                res += x[i]
                i += 1
            while j<=len(y)-1 and y[j] != c:
                res += y[j]
                j += 1
            res += c
            i, j = i + 1, j + 1

        return ( res + x[i:] + y[j:])
    def solve(self,x,y)->str:
        arr=[["" for i in range(len(y)+1)]for j in range(len(x)+1)]
        for i in range(1,len(x)+1):
            for j in range(1,len(y)+1):
                if x[i-1]==y[j-1]:
                    arr[i][j]= x[i-1]+arr[i-1][j-1]
                else:
                    #arr[i][j]=max(arr[i-1][j],arr[i][j-1])
                    s1= arr[i-1][j]
                    s2= arr[i][j-1]
                    if len(s1)>len(s2):
                        arr[i][j]=s1
                    else:
                        arr[i][j]=s2
        return arr[len(x)][len(y)]
x='AGGTAB'
y='GXTXAYB'
ans= Solution()
print(ans.lcs(x,y))



# Recursive
# class Solution:
#     def lcs(self,x,y):
#         st= self.solve(x,y)
#         return st[::-1]
#     def solve(self,x,y)->str:
#         if len(x)==0 or len(y)==0:
#             return ""
#         if x[len(x)-1]==y[len(y)-1]:
#             return x[len(x)-1]+self.solve(x[0:len(x)-1],y[0:len(y)-1])
#         else:
#             s1= self.solve(x[0:len(x)-1],y)
#             s2= self.solve(x,y[0:len(y)-1])
#             if len(s1)>len(s2):
#                 return s1
#             else:
#                 return s2
