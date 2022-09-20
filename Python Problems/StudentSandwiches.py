from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length= len(students)
        i=0
        j=0
        count=0
        rotation=0
        while len(students)!=0:
            if students[i]==sandwiches[j]:
                rotation=0
                count=count+1
                students.pop(0)
                sandwiches.pop(0)
            else:
                rotation=rotation+1
                temp=students.pop(0)
                students.append(temp)
                if rotation==len(students):
                    break;
        return abs(count-length)

ans=Solution()
print(ans.countStudents([1,1,1,0,0,1],[1,0,0,0,1,1]))   