from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        vector=[]
        i,j=0,0
        k=len(p)
        anagram={}
        copy={}
        for alpha in p:
            if alpha in anagram:
                copy[alpha]=copy[alpha]+1
                anagram[alpha]=anagram[alpha]+1
            else:
                copy[alpha]=1
                anagram[alpha]=1
        count=len(anagram)
        while j<len(s) and i <len(s):
            if s[j] in anagram:
                anagram[s[j]]=anagram[s[j]]-1
                if anagram[s[j]]==0:
                    count=count-1
            if j-i+1!=k:
                j+=1
            else:
                if count==0:
                    vector.append(i)
                if s[i] in anagram:
                    anagram[s[i]]=anagram[s[i]]+1   
                    if anagram[s[i]]==1:
                        count=count+1
                i=i+1
                j=j+1
        return vector
ans= Solution()
ans.findAnagrams(s = "cbaebabacd", p = "abc")
