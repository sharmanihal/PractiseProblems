from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]):
        i=0
        count=0
        m=n=len(intervals)
        intervals.sort(key=lambda x: (x[0]))
        while i<n-1:
            if intervals[i][1]>intervals[i+1][0] and intervals[i][0]<=intervals[i+1][1]:
                if intervals[i][1]>intervals[i+1][1]:
                    intervals.pop(i)
                else:
                    intervals.pop(i+1)
                count=count+1
                n=n-1
            else:
                i=i+1
        return count

ans= Solution()
print(ans.merge( [[1,100],[11,22],[1,11],[2,12]]))
        
