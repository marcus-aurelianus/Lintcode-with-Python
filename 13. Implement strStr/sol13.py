class Solution:
    def strStr(self,source,target):
        n,m=len(source),len(target)
        for i in range(n-m+1):
            if source[i:i+m]==target:
                return i
        return -1

#Test Cases:
    
sol=Solution()
print(sol.strStr("source","target"))
