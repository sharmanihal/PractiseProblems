from tkinter.messagebox import RETRY
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i=0
        j=0
        n=1
        while i<=len(s)-1:
            if j<=len(spaces)-1 and i==spaces[j]:
                s=s[0:spaces[j]]+' '+s[spaces[j]:]
                j=j+1
                if j<=len(spaces)-1:
                    spaces[j]=spaces[j]+n
                    n=n+1
            i=i+1 
        return s
    #0123456789012   

ans= Solution()
# print(ans.addSpaces(s,spaces))
