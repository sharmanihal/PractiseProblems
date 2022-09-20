class Solution:
    def findSubstringWithMostVowels(self, s: str,k:int) -> str:
        i=0
        j=k-1
        count=0
        index=[0,0]
        once=True
        while(i<=j):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                count=count+1;
                if(once):
                    index[0]=i
                    index[1]=j
                    once=False
            i=i+1
        i=0
        j=k-1
        prevCount=count;
        while j<len(s)-1 and j-i==k-1:
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                count=count-1
                i=i+1
            else :
                i=i+1
            
            if s[j+1]=='a' or s[j+1]=='e' or s[j+1]=='i' or s[j+1]=='o' or s[j+1]=='u':
                count=count+1;
                j=j+1
            else:
                j=j+1
            
            if prevCount<count:
                prevCount=count
                index[0]=i
                index[1]=j
        return prevCount
        # if index[0]==0 and index[1]==0:
        #     return ""
        # return s[index[0]:index[1]+1]

ans=Solution()
print(ans.findSubstringWithMostVowels("hbhg",3))