from audioop import reverse
from math import fabs
from typing import List


class Solution:
    def wordBreak(self,s, words):
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in words:
                if d[i]:
                    break
                if  (d[i-len(w)] or i-len(w) == -1) and w == s[i-len(w)+1:i+1] :
                    d[i] = True
        return d[-1]

ans= Solution()
print(ans.wordBreak("cars",["car","ca","rs"]))