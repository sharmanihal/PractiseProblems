class Solution:
    
    def countVowelStrings(self, n: int) -> int:
        memo=[1 for i in range(5)]
        k=1
        j=0
        for i in range(n):
            k=1
            j=0
            for q in range(4):
                memo[k]=memo[j]+memo[k]
                j=j+1
                k=k+1
        return memo[len(memo)-1]
ans= Solution()
print(ans.countVowelStrings(1))









# #
# class Solution:
#     def __init__(self) -> None:
#         self.count=0
#         self.arr=[[-1 for i in range(6)]for j in range(6)]
#     def countVowelStrings(self, n: int) -> int:
#         self.solve(5,n,0,0)
#         return self.count
#     def solve(self,s,n,i,str):
#         if i>s-1 or str==n:
#             return str
#         if self.arr[i][str]!=-1:
#             return self.arr[i][str]
            
#         if self.solve(s,n,i,str+1):
#             self.count=self.count+1
#         self.solve(s,n,i+1,str)
# ans= Solution()
# print(ans.countVowelStrings(5))

