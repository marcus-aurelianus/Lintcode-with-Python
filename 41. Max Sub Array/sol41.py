class Solution:
    def maxSubArray(self,nums):
        if nums is None or len(nums)==0:
            return 0
        n=len(nums)
        local=max_local=nums[0]
        for i in range(1,n):
            max_local=nums[i]+max(0,max_local)
            local=max(local,max_local)
        return local

#Test Case:
sol=Solution()
lst=[-50,-1,1,-2,-3,-100,-1,4,-50]
print(sol.maxSubArray(lst))
