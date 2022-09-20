from typing import List


class Solution:
    arr=[]
    def allSubset(self,ip,op):
        if len(ip)==0:
            print(op)
            return
        op1=op
        op2=op
        op2=op+ip[0]
        ip=ip[1:]
        self.allSubset(ip,op1)
        self.allSubset(ip,op2)
        return

    def allSubsetOfArray(self,nums,op=[]):
        if len(nums)==0:
            self.arr.append(op)
            return
        op1 = list(op)
        op2 = list(op)
        op2.append(nums[0])
        nums=nums[1:]
        # print('op1 : ',op1," op2: ",op2," ip: ",nums)
        self.allSubsetOfArray(nums,op1)
        self.allSubsetOfArray(nums,op2)
        return self.arr

ans= Solution()
# ans.allSubset("ab","")
print(ans.allSubsetOfArray([1,2,3,4]))