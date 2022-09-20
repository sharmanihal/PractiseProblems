from typing import List


class Solution:
    def __init__(self) -> None:
        self.score1=0
        self.score2=0
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.solve(0,0,nums,1)
        return self.score1>=self.score2
    def solve(self,player1,player2,nums,turn):
        self.score1=player1
        self.score2=player2
        if len(nums)==0:
            if player1>=player2:
                return True
            return False
        if turn==1:
            op1=player1+nums[0]
            if self.solve(op1,player2,nums[1:],2)==False and len(nums)!=1:
                op2= player1+nums[len(nums) - 1]
                return self.solve(op2,player2,nums[0:len(nums)-1],2)
            return False
        if turn==2:
            op1=player2+nums[0]
            if self.solve(player1,op1,nums[1:],1)==True and len(nums)!=1:
                op2= player2+nums[len(nums) - 1]
                return self.solve(player1,op1,nums[0:len(nums)-1],1)
            return True
ans= Solution()
print(ans.PredictTheWinner([1,]))


