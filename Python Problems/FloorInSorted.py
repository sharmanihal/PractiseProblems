from turtle import begin_fill


class Solution:
    def findFloor(self,arr,x):
        start=0
        end= len(arr)-1
        mid=-1

        save=-1
        while start<=end:
            mid=int((start+end)/2)
            if arr[mid]==x:
                save= mid
                break
            if arr[mid]>x:
                end=mid-1
            if arr[mid]<x:
                start=mid+1
        if(save==-1):
            return [-1,-1]
        begin=save
        last=save
        while begin >=0 and arr[begin]==x:
            begin=begin-1
        

        while last<= len(arr)-1 and arr[last]==x:
            last=last+1
        return [begin,last]
            

ans= Solution()
print(ans.findFloor([5,7,7,8,8,10], x = 10))