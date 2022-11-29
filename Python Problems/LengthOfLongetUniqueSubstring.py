class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word={}
        i,j=0,0
        maxLength=0
        while j<len(s):
            if s[j] in word:
                word[s[j]]=word[s[j]]+1
            else:
                word[s[j]]=1
            if len(word)==j-i+1:
                maxLength=max(maxLength,j-i+1)
                j=j+1
            elif len(word)<j-i-1:
                while len(word)<j-i-1:
                    word[s[i]]-=1
                    if word[s[i]]==0:
                        word.pop(s[i])
                    i=i+1
                j=j+1
        return maxLength
    def maxsub(self,s):
        i,j,maxLength=0,0,0
        word={}
        while j<len(s):
            if s[j] in word:
                word[s[j]]=word[s[j]]+1
            else:
                word[s[j]]=1
            if len(word)==j-i+1:
                maxLength=max(maxLength,j-i+1)
                j=j+1
            elif len(word)<j-i+1:
                while len(word)<j-i+1:
                    word[s[i]]-=1
                    if word[s[i]]==0:
                        word.pop(s[i])
                    i=i+1
                j=j+1
        return maxLength
ans= Solution()
print(ans.lengthOfLongestSubstring("pwwkew"))