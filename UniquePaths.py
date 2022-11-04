class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr=[[-1 for i in range(n+1)]for j in range(m+1)]
        for i in range(m+1):
            arr[i][1]=1
        for j in range(n+1):
            arr[1][j]=1
        return self.solve(m,n,arr)
    def solve(self,m,n,arr):
        if arr[m][n]!=-1:
            return arr[m][n]
        for i in range(2,m+1):
            for j in range(2,n+1):
                arr[i][j]=arr[i-1][j]+ arr[i][j-1]
        return arr[m][n]
    
ans= Solution()
print(ans.uniquePaths(3,2))