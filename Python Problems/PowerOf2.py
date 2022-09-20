class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<2:
            return False
        if n==2:
            return True
        return self.isPowerOfTwo(n/2)
ans=Solution()
print(ans.isPowerOfTwo(1))
        