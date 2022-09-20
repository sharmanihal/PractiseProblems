class Solution:
    def lastRemaining(self, n: int) -> int:
        arr=[]
        sum=0
        length= n
        odd=0
        even=0
        # while length!=1:

        for i in range(n):
            if i%2==0:
                odd= odd+i
            else:
                even=even+i
            sum=sum+i
            arr.append(i+1)
        print(sum)
        return self.solve(arr,turn='left')








        
    def solve(self,arr,turn):
        print(arr)
        if len(arr)==1:
            return arr[0]
        
        if turn=='left':
            newarr=[]
            i=0
            while i<=len(arr)-1:
                if i!=0 and i%2!=0:
                    newarr.append(arr[i])
                i=i+1
            return self.solve(newarr,'right')
        else:
            newarr=[]
            j=len(arr)-1
            boo= len(arr)%2==0
            while j>=0:
                if boo and j%2==0:
                    newarr.append(arr[j])
                elif not boo and j%2!=0:
                    newarr.append(arr[j])
                j=j-1
            newarr.reverse()
            return self.solve(newarr,'left')

                    
ans= Solution()
print(ans.lastRemaining(5))