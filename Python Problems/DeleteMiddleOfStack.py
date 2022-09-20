from math import ceil


class Solution:
    def middle(self,s):
        if len(s)==0:
            return s
        k= ceil(len(s)/2)+1
        self.deleteMid(s,k)
        return s
    def deleteMid(self, s, k):
        if k==1:
            s.pop()
            return
        temp=s.pop()
        self.deleteMid(s,k-1)
        s.append(temp)

ans= Solution()
print(ans.middle([5,4,3,2,1],5))