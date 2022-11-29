class Solution:
    def longest(self,s,k):
        word={}
        unique=0
        i,j=0,0
        maxLength=0
        while j<len(s) and i<len(s):
            if s[j] in word:
                word[s[j]]=word[s[j]]+1
            else:
                word[s[j]]=1
                unique=unique+1
            if unique<k:
                j=j+1
            elif unique==k:
                if maxLength<j-i+1:
                    maxLength=j-i+1
                j=j+1
            elif unique>k:
                while unique>k:
                    if s[i] in word:
                        if word[s[i]]==1:
                            word.pop(s[i])
                            unique=unique-1
                        elif word[s[i]]>1:
                            word[s[i]]=word[s[i]]-1
                    i=i+1
                j=j+1
        return maxLength
ans= Solution()
print(ans.longest('aabacbebebe',3))



