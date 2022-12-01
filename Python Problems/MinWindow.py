import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i,j=0,0
        freq={}
        maxLength=sys.maxsize
        finalI, finalJ=0,0
        for alpha in t:
            if alpha in freq:
                freq[alpha]=freq[alpha]+1
            else:
                freq[alpha]=1
        count=len(freq)
        while j<len(s):
            print(freq,count)
        
            if s[j] in freq :
                freq[s[j]]=freq[s[j]]-1
                if freq[s[j]]==0:
                    count=count-1
            if count>0:
                j=j+1
            elif count==0:
                while count==0:
                    if maxLength>j-i+1:
                        maxLength=j-i+1
                        finalI=i
                        finalJ=j
                    if s[i] in freq:
                            freq[s[i]]=freq[s[i]]+1
                            if freq[s[i]]>0:
                                count=count+1
                            i=i+1  
                    else:
                        i=i+1
                j=j+1
            
        print(s[finalI:finalJ+1],i,j)
ans= Solution()
ans.minWindow( s = "ADABECODEBANC", t = "ABC")                  

# A-1 count=1
# B-0
# C-0

# Input: s = "ADABECODEBANC", t = "ABCA"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.