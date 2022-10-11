from sys import maxsize
class Solution :
    def __init__(self) -> None:
        self.dp=[[-1 for i in range(1001)]for i in range(1001)]
    def mcm(self,arr)->int:
        return self.solve(arr,1,len(arr)-1)
    def solve(self,arr,i,j):
        if i>=j:
            # i>j means that there are no elemenst in the array, 
            # i=j means there is only one element in array which is also not valid a there should be 2 dimensions
            return 0
        if self.dp[i][j]!=-1:
            return self.dp[i][j]
        k=i
        min=maxsize
        while k<=j-1:
            temp= self.solve(arr,i,k)+ self.solve(arr,k+1,j)+ (arr[i-1]*arr[k]*arr[j])
            #the two solve will give us e.g AB and BC to find final cost AB * BC we do (arr[i-1]*arr[k]*arr[j])
            if temp<min:
                min=temp
                self.dp[i][j]=min
            k=k+1
        return self.dp[i][j]
ans = Solution()
print(ans.mcm([40,20,30,10,30]))