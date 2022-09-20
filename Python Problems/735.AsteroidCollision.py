from heapq import heappop, heappush
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        vector=[]
        for i in range(len(asteroids)-1,-1,-1):
            if len(stack)==0 and asteroids[i]>0:
                vector.append((i,asteroids[i]))
                continue
            elif len(stack)==0 and asteroids[i]<0:
                stack.append((i,asteroids[i]))
                continue
            elif len(stack)>0 and stack[len(stack)-1][1]<0 and asteroids[i]>0:
                while len(stack)>0 and stack[len(stack)-1][1]<0 and asteroids[i]>0 and stack[len(stack)-1][1]+asteroids[i]>0:
                    stack.pop()
                    
                if len(stack)>0 and stack[len(stack)-1][1]+asteroids[i]==0:
                    stack.pop()
                    continue
                elif len(stack)>0 and stack[len(stack)-1][1]+asteroids[i]>0:
                    stack.append((i,asteroids[i]))
                    continue
                if len(stack)==0:
                    stack.append((i,asteroids[i]))
                    continue

            elif len(stack)>0 and stack[len(stack)-1][1]<0 and asteroids[i]<0:
                stack.append((i,asteroids[i]))
                continue

            elif len(stack)>0 and stack[len(stack)-1][1]>0 and asteroids[i]<0:
                stack.append((i,asteroids[i]))
                continue

            elif len(stack)>0 and stack[len(stack)-1][0]>0 and asteroids[i]>0:
                stack.append((i,asteroids[i]))
                continue
        heap=[]
        for i in stack+vector:
            heappush(heap,i)
        arr=[]
        for i in range(len(heap)):
            arr.append(heappop(heap)[1])
        return (arr)

ans=Solution()
print(ans.asteroidCollision([2,-1,2,-1]))