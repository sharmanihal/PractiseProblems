from sys import maxsize
class Solution:
    def __init__(self) -> None:
        self.it=0
        self.arr=[[]]
    def minCut(self, s: str) -> int:
        
        self.solve(s,0,len(s)-1)
        print( self.arr)
    def solve(self,s,i,j):
        if i>j :return 
        if self.isPalindrome(s,i,j): 
            self.arr[self.it].append(s[i:j+1]) 
            return
        k=i
        while k<=j-1:
            self.solve(s,i,k)
            self.solve(s,k+1,j)
            k=k+1
        self.arr.append([])
        self.it=self.it+1
        return 
    def isPalindrome(self,s,i,j):
        if i>=j :return True
        while i<j: 
            if s[i]!=s[j] : 
                return False
            i=i+1
            j=j-1
        return True

ans= Solution()
ans.minCut('abccb')



