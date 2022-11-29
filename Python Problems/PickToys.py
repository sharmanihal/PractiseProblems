from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
	#This map keeps track of the types of the fruits
        fruitTypes={}
        i,j=0,0
        maxLength=0
        while j<len(fruits):
		#If a fruit is already present in the map , increse the count of that fruit in the map
            if fruits[j] in fruitTypes:
                fruitTypes[fruits[j]]=fruitTypes[fruits[j]]+1
			#If a fruit is not  present in the map ,set its count as one
            else:
                fruitTypes[fruits[j]]=1
			#If the length of the map is less than or equal to 2 that means we are not out of boundary
            #case #which states that we can only pick 2 types of fruits, so just store the max length (length of winodow)
            # and #increase j to go to next fruit in the line.
            if len(fruitTypes)<=2:
                maxLength=max(maxLength,j-i+1)
                j=j+1
		    #Now if the length of the map increase more than 2, that means we have voliated a condition of
            #picking only two types of fruits, so in that case we will remove the fruit from the left using i. 
            #To remove the fruit we will check if it present in the map and what is the count of that fruit. 
            # If the count if 1, than remove #the fruit altogether from the basket, else if the count is more than 1 , 
            # dercrease the count by 1 and the #increase i until the length of the map is not equal of less than 2.
            elif len(fruitTypes)>2:
                while len(fruitTypes)>2:
                    if fruits[i] in fruitTypes:
                        if fruitTypes[fruits[i]]==1:
                            fruitTypes.pop(fruits[i])
                        elif fruitTypes[fruits[i]]>1:
                            fruitTypes[fruits[i]]=fruitTypes[fruits[i]]-1
                    i=i+1
                j=j+1
		#Return the max length calculated
        return maxLength