#o(n^2) brute force approach
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            sum=0
            for j in range(i,len(nums)):
                sum+=nums[j]
                if sum==k:
                    count+=1
        return count
        
        

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map={}
        map[0]=1
        sum=0
        count=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            if sum-k in map:
                count+=map[sum-k]
            map[sum]=map.get(sum,0)+1
        return count