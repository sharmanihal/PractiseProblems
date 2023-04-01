from typing import List


class Solution:
    def leastBricks(self, walls: List[List[int]]) -> int:
        #so instead of us goig through each postion one by one and cut the brick from there
        #we will calculate the max number of gaps in each postion of the row
        #the position with most gaps across all rows will be the corrcet place to cut the bricks
        map={}
        totalSum=sum(walls[0])
        for i in walls:
            sums=0
            for j in i:
                sums+=j
                if sums==totalSum:
                    continue
                if sums in map:
                    map[sums]+=1
                else:
                    map[sums]=1
        maxVal=0
        for i in map:
            maxVal=max(maxVal,map[i])
        return len(walls)-maxVal
                
                    
            
                    