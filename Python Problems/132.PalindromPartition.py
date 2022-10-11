from sys import maxsize
class Solution:
    def __init__(self) -> None:
        self.dp=[[-1 for i in range(2001)]for j in range(2001)]
    def minCut(self, s: str) -> int:
        return self.solve(s,0,len(s)-1)
    def solve(self,s,i,j):
        if i>=j or self.isPalindrome(s,i,j): return 0
        if self.dp[i][j]!=-1 : return self.dp[i][j]
        k=i
        ans= maxsize
        while k<=j-1:
            if self.isPalindrome(s,i,k):
                ans = min(ans,self.solve(s,k+1,j)+1)
            k=k+1
        self.dp[i][j]=ans
        return ans
    def isPalindrome(self,s,i,j):
        if i>=j :return True
        while i<j: 
            if s[i]!=s[j] : 
                return False
            i=i+1
            j=j-1
        return True

ans= Solution()
print(ans.minCut('abacb'))

