class Solution:
    def countSubstrings(self, s: str) -> int:
        arr=[[-1 for i in range(len(s))]for j in range(len(s))]
        count =0
        for i in range(len(s)):
            for j in range(i,len(s)):
                count+=self.checkPalindrome(s,i,j,arr)
        return count
    def checkPalindrome(self,s,i,j,arr):
        if i>=j:
            return 1
        if arr[i][j]!=-1:
            return arr[i][j]
        if s[i]==s[j]:
            arr[i][j]= self.checkPalindrome(s,i+1,j-1,arr)
        else:
            arr[i][j]=0
        return arr[i][j]

ans = Solution()
ans.countSubstrings('nitin') 