import sys


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq={}
        finalI,finalJ=-1,-1
        
        for word in s1:
            if word in freq:
                freq[word]+=1
            else:
                freq[word]=1
        count=len(freq)
        maxlength=sys.maxsize
        i,j=0,0
        while j<len(s2):
            if s2[j] in freq:
                freq[s2[j]]=freq[s2[j]]-1
                if freq[s2[j]]==0:
                    count=count-1
            if count>0:
                j=j+1
            elif count==0:
                if maxlength>j-i+1:
                    maxlength=min(maxlength,j-i+1)
                    finalI=i
                    finalJ=j
                while count==0:
                    if s2[i] in freq:
                        freq[s2[i]]+=1
                        if freq[s2[i]]==1:
                            if maxlength>j-i+1:
                                maxlength=j-i+1
                                finalI=i
                                finalJ=j
                            count=count+1
                        i=i+1
                    else:
                        i=i+1
                j=j+1
            print(finalI,finalJ)
            if finalJ-finalI+1==len(s1) :
                return True
            else:False

s1 ="h"

s2 = "jrfrspuz"
ans= Solution()
print(ans.checkInclusion(s1,s2))