import sys
from typing import List

#Recursive
class Solution:
    ##Varition of unbounded knapsack where we can selete 1 coins as many times a we want
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo=[[-1 for i in range(amount+1)]for j in range(len(coins)+1)]
        for i in range(amount+1):
            memo[0][i]=sys.maxsize-1
        for i in range(len(coins)+1):
            memo[i][0]=0
        res= self.unboundeKnapsack(coins,amount,memo)
        if res==sys.maxsize-1:
            return -1
        else:
            return res
    def unboundeKnapsack(self,coins,amount,memo):
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    memo[i][j]= min(1+memo[i][j-coins[i-1]],memo[i-1][j])
                else:
                    memo[i][j]= memo[i-1][j]
        return memo[len(coins)][amount]
ans=Solution()
print(ans.coinChange(coins = [1,2,5], amount = 11))