class Solution:
    def rotateString(self,str,offset):
        pos=offset%(len(str))
        return str[-pos:]+str[:-pos]


#Test Cases:
    
sol=Solution()
print(sol.rotateString("abcdefg",3))
