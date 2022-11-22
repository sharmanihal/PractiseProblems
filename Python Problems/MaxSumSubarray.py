class SOlution:
    def maxSumSubArray(self,nums:list,k:int)->int:
        i=0
        sum=0
        max=0
        j=-1
        for x in range(k):
            j=j+1
            sum=sum+nums[j]
        while j<len(nums):
            if sum>max:
                max= sum
            sum= sum-nums[i]
            i=i+1
            j=j+1
            if j>=len(nums):
                break
            sum=sum+nums[j]
        print(max)

ans= SOlution()
ans.maxSumSubArray([100, 200, 300, 400],4)