class Solution:
    def strStr(self,source,target):
        if source==None or target==None:
            return -1
        n,m=len(source),len(target)
        for i in range(n-m+1):
            if source[i:i+m]==target:
                return i
        return -1

#Test Cases:
    
sol=Solution()
print(sol.strStr(null,"target"))
