class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j= 0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i=i+1
            j=j+1
        if i==len(s):return True
        else: return False
ans= Solution()
ans.isSubsequence('abc','ahbgdc')
