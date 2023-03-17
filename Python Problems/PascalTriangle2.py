class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        vector=[[1]]
        for i in range(1,numRows):
            if i==1:
                vector.append([1,1])
            else:
                temp=[1]
                k,x=0,1
                while x<len(vector[i-1]):
                    temp.append(vector[i-1][k]+vector[i-1][x])
                    k+=1
                    x+=1
                temp.append(1)
                vector.append(temp)
        return vector
                
