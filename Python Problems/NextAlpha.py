from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start=0
        end=len(letters)-1
        mid=-1
        save=''
        while start<=end:
            mid=int((start+end)/2)
            if letters[mid]>target:
                save=letters[mid]
            if letters[mid]>target:
                end=mid-1
                continue
            if letters[mid]<=target:
                start=mid+1
                continue
        if save=='':
            return letters[0]
        else :
            return save
ans=Solution()
print(ans.nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"],"e"))