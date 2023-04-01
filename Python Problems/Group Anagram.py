class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            #We create a array for each string of str
            count=[0]*26
            for c in s:
                #Then we count the occrance of each character, then this array is considered as a 
                #key i.e, anagram will have same key (same array)
                count[ord(c)-ord("a")]+=1
            #using the list that we calculated above we append the anagram to the map.
            res[tuple(count)].append(s)
        return res.values()
        
                
