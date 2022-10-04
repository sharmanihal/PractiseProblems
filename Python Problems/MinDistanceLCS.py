class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        str= self.LCS(word1,word2)
        l1= len(word1)-str
        l2=len(word2)-str
        return l1+l2
    def LCS(self,x,y):
        arr=[[-1 for i in range(len(y)+1)]for j in range(len(x)+1)]
        for j in range(len(y)+1):
            arr[0][j]=0
        for i in range(len(x)+1):
            arr[i][0]=0
        for i in range(1,len(x)+1):
            for j in range(1,len(y)+1):
                if x[i-1]==y[j-1]:
                    arr[i][j]=1+arr[i-1][j-1]
                else:
                    arr[i][j]=max(arr[i][j-1],arr[i-1][j])
        return arr[len(x)][len(y)]
        

ans= Solution()
print(ans.minDistance('leetcode','etco'))
