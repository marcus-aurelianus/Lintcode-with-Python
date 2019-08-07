class Solution:
    def productExcludeItself(self,nums):
        n=len(nums)
        res=[]
        def helper(lsts):
            res=1
            for i in range(len(lsts)):
                res*=lsts[i]
            return res
        for i in range(n):
            res.append(helper(nums[:i])*helper(nums[i+1:]))
        return res
        
#Test Case:
sol=Solution()
lst=[1,2,3]
print(sol.productExcludeItself(lst))
