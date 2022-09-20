class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,arr, n, k):
        #code here
        res=-1
        start,end=self.findMaxAndSum(arr)
        while start<=end:
            mid=int((start+end)/2)
            if self.isValidScheme(arr,mid,k)==True:
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res
    def isValidScheme(self,arr,mid,k):
        student=1
        sum=0
        for i in arr:
            sum=sum+i
            if sum>mid:
                student=student+1
                sum=i
            if student>k:
                return False
        return True

    def findMaxAndSum(self,arr):
        max=0
        sum=0
        for i in arr:
            if i>max:
                max=i
            sum=sum+i
        return max,sum
ans=Solution()
print(ans.findPages([10,20,30,40],4,2))