from copyreg import constructor
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth=0
        for i in logs:
            if i=="../":
                if depth==0:
                    depth=0
                else:
                    depth=depth-1;
                continue
            if i=="./":
                continue
            else:
                depth=depth+1
                print(depth,i)
        

ans=Solution()
list=["d1/","d2/","../","d21/","./"]
print(ans.minOperations(list))

print(list[2]=='../')



# class Solution:
#     def minAddToMakeValid(self, s: str) -> int:
#         stack=[]
#         count =0;
#         for i in s:
#             if i=='(':
#                 stack.append('(')
#             if i==')':
#                 if(len(stack)==0):
#                     count=count+1;
#                 else:
#                     stack.pop();
#         if len(stack)!=0:
#             return len(stack)
#         else:
#             return count