from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum=0
        for i in arr:
            sum=sum+i
        if len(arr)%2!=0:
            sum=2*sum
            