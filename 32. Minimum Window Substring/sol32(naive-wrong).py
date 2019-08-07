class Solution:
    def minWindow(self,source,target):
        start,end=0,len(source)
        def helper(str1,str2):
            for ele in str2:
                if str2.count(ele)>str1.count(ele) or ele not in str1:
                    return False
            return True
        while start<=end and helper(source[start:end],target):
            start+=1
        start-=1
        while start<=end and helper(source[start:end],target):
            end-=1
        end+=1
        return source[start:end]


#Test Case
source='absdfaabab'
target="adb"
sol=Solution()
print(sol.minWindow(source,target))
