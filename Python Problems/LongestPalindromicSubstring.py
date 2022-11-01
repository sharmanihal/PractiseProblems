from re import L


class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen=0
        l1,r1=0,0
        l2,r2=0,0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    l1=l
                    r1=r
                    resLen=r-l+1
                l=l-1
                r=r+1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    l2=l
                    r2=r
                    resLen=r-l+1
                l=l-1
                r=r+1
        if r1-l1>r2-l2:
            return s[l1:r1+1]
        else:
            return s[l2:r2+1]
ans= Solution()
print(ans.longestPalindrome('babad'))