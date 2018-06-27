class Solution:
    def rotateString(self,s,offset):#wrong q, string cannot do value assignment...
        if len(s)>0:
            offset=offset%(len(s))
        temp=s[-offset:]+s[:-offset]
        for i in range(len(temp)):
            s[i]=temp[i]

#Test Cases:
    
sol=Solution()
a="abcdefg"
sol.rotateString(a,3)
print(a)
