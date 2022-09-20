class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s=self.solve(n)
        return s[k-1]
    def solve(self, n: int) -> str:
        if n==1:
            return '0'
        s=self.solve(n-1)
        s1=''.join('1' if x == '0' else '0' for x in s)[::-1]
        s=s+'1'
        s=s+s1
        return s
ans= Solution()
print(ans.findKthBit(4,11))
        
