class Solution:
    def firstInWindow(self,nums,k):
        vector=[]
        neg=[]
        i,j=0,0
        while j<len(nums) and i<len(nums):
            if nums[j]<0:
                neg.append(nums[j])
            if j-i+1!=k:
                j=j+1
            else:
                if len(neg)==0:
                    vector.append(0)
                else:
                    vector.append(neg[0])
                    if nums[i]==neg[0]:
                        neg=neg[1:]
                i=i+1
                j=j+1
        return vector
ans= Solution()
ans.firstInWindow([12, -1, -7, 8, -15, 30, 16, 28], 3)
