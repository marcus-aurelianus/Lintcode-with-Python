class Solution:
    def maxTwoSubArrays(self,nums):
        if nums is None or len(nums)==0:
            return 0
        n=len(nums)
        sub1,sub2,sub3,sub4,=[0]*n,[0]*n,[0]*n,[0]*n
        sub1[0]=sub3[0]=nums[0]
        sub2[n-1]=sub4[n-1]=nums[n-1]
        for i in range(1,n):
            sub1[i]=nums[i]+max(0,sub1[i-1])
            sub3[i]=max(sub3[i-1],sub1[i])
            sub2[n-i-1]=nums[n-i-1]+max(0,sub2[n-i])
            sub4[n-i-1]=max(sub4[n-i],sub2[n-i-1])
        res=sub3[0]+sub4[1]
        print(sub1,sub2)
        print(sub3,sub4)
        for i in range(1,n-1):
            res=max(sub3[i]+sub4[i+1],res)
        return res 

#Test Case:
sol=Solution()
lst=[-1,-2,-3,-100,-1,-50]
print(sol.maxTwoSubArrays(lst))
