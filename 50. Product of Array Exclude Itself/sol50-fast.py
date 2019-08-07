class Solution:
    def productExcludeItself(self,nums):
        n=len(nums)
        res=[1]*n
        prod, prod_rever = 1, 1
        for i in range(n):
            res[i]*=prod
            prod*=nums[i]
            res[n-1-i]*=prod_rever
            prod_rever*=nums[n-1-i] 
        return res
            
        
#Test Case:
sol=Solution()
lst=[1,2,3]
print(sol.productExcludeItself(lst))
