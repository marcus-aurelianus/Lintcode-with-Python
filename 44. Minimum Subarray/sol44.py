class Solution:
    """
    An adaption of Kadane's algro.
    """
    def minSubArray(self,nums):
        if nums is None or len(nums)==0:
            return 0
        n=len(nums)
        local=min_local=nums[0]
        for i in range(1,n):
            min_local=nums[i]+min(0,min_local)
            local=min(local,min_local)
        return local
#Test Case:
sol=Solution()
lst=[1,-1,-2,1]
print(sol.minSubArray(lst))
