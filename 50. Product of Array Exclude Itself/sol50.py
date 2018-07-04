class Solution:
    def productExcludeItself(self,nums):
        n=len(nums)
        res=[1]*n
        def helper(lsts):
            res=1
            for i in range(len(lsts)):
                res*=lsts[i]
            return res
        for i in range(n):
            res[i]=helper(lst[:i])*helper(lst[i+1:])
        return res
        
#Test Case:
sol=Solution()
lst=[1,2,3]
print(sol.productExcludeItself(lst))
