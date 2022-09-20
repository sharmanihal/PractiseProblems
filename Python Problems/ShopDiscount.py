
from typing import List

from numpy import append
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        vector=[]
        stack=[]
        for i in range( len(prices) - 1, -1, -1) :
            if(len(stack)==0):
                vector.append(prices[i])
            elif len(stack)>0 and stack[len(stack)-1]<=prices[i]:
                vector.append(prices[i]-stack[len(stack)-1])
            elif len(stack)>0 and stack[len(stack)-1]>prices[i]:
                while len(stack)>0 and stack[len(stack)-1]>prices[i]:
                    stack.pop()
                if(len(stack)==0):
                    vector.append(prices[i])
                else:
                    vector.append(prices[i]-stack[len(stack)-1])
            stack.append(prices[i])
        vector.reverse()
        return vector
        
        
ans= Solution()
print(ans.finalPrices([10,2,5,2,8]))