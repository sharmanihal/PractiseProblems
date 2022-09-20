from ast import Num
from turtle import st
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        vector=[]
        for i in range( len(nums2) - 1, -1, -1) :
            if len(stack)==0:
                vector.append(-1)
            if len(stack)>0 and stack[len(stack)-1]>nums2[i]:
                vector.append(stack[len(stack)-1])
            if len(stack)>0 and stack[len(stack)-1]<=nums2[i]:
                while len(stack)>0 and stack[len(stack)-1]<=nums2[i]:
                    stack.pop()
                if len(stack)==0:
                    vector.append(-1)
                else:
                    vector.append(stack[len(stack)-1])
            stack.append(nums2[i])
        vector.reverse()
        #here we are using hashmap to get elemenst
        dict={}
        for i in range(len(nums2)):
            dict[nums2[i]]=vector[i]
        arr=[]
        for i in nums1:
            arr.append(dict[i])
        return arr
ans= Solution()
print(ans.nextGreaterElement([4,1,2],[1,3,4,2]));