class Solution:
    def towerOfHanoi(self,source,dest,helper,n):
        if n==1:
            print('Moving '+str(n)+ ' from '+ str(source) +" to "+ str(dest))
            return
        self.towerOfHanoi(source,helper,dest,n-1)
        print('Moving '+str(n)+ ' from '+ str(source) +" to "+ str(dest))
        self.towerOfHanoi(helper,dest,source,n-1)
        return
ans= Solution()
ans.towerOfHanoi(1,2,3,4)