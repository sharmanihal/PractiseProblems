from tkinter.tix import Tree


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.LCS(s,s[::-1])
    def LCS(self,x,y)->str:
        max=""
        arr=[["" for i in range(len(y)+1)]for j in range(len(x)+1)]
        for i in range(1,len(x)+1):
            for j in range(1,len(y)+1):
                if x[i-1]==y[j-1]:
                    
                    arr[i][j]=x[i-1]+arr[i-1][j-1]
                else:
                    arr[i][j]=""
                if len(arr[i][j])>len(max) and self.isPalindrome(arr[i][j]):
                    max=arr[i][j]
        return max
    def isPalindrome(self,s):
        if len(s)==1:
            return True
        if len(s)%2==0:
            l=len(s)//2
            i=l-1
            j=l
            while i>0 and j<len(s):
                if s[i]!=s[j]:
                    return False
                else:
                    i=i-1
                    j=j+1
            return True
        else:
            l=len(s)//2
            i=l-1
            j=l+1
            while i>=0 and j<len(s):
                if s[i]!=s[j]:
                    return False
                else:
                    i=i-1
                    j=j+1
            return True
ans= Solution()
print(ans.longestPalindrome("abcba"))
print(ans.isPalindrome('caa'))

