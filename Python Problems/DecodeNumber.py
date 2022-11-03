class Solution:
    def numDecodings(self, s: str) -> int:
        arr=[]
        dp=[False]*len(s)
        for i in range(1,27):
            arr.append(str(i))
        for i in range(len(s)):
            for w in arr:
                if (dp[i-len(w)] or i-len(w)==-1) and w==s[i-len(w)+1:i+1]:
                    dp[i]=True
                
        print(dp)

ans = Solution()
ans.numDecodings('226')
