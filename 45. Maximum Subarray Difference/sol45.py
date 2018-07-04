class Solution:
    def maxDiffSubArray(self,nums):
        if nums is None or len(nums)==0:
            return 0
        n=len(nums)
        max1,subx1,max2,subx2,=[0]*n,[0]*n,[0]*n,[0]*n
        min1,subn1,min2,subn2,=[0]*n,[0]*n,[0]*n,[0]*n
        max1[0]=min1[0]=subx1[0]=subn1[0]=nums[0]
        max2[n-1]=min2[n-1]=subx2[n-1]=subn2[n-1]=nums[n-1]
        for i in range(1,n):
            max1[i]=nums[i]+max(0,max1[i-1])
            subx1[i]=max(max1[i],max1[i-1])
            min1[i]=nums[i]+min(0,min1[i-1])
            subn1[i]=min(min1[i],min1[i-1])
            
            max2[n-i-1]=nums[n-i-1]+max(0,max2[n-i])
            subx2[n-i-1]=max(max2[n-i-1],max2[n-i])
            min2[n-i-1]=nums[n-i-1]+min(0,min2[n-i])
            subn2[n-i-1]=min(min2[n-i-1],min2[n-i])
        res=max(abs(subx1[0]-subn2[1]),abs(subn1[0]-subx2[1]))
        for i in range(1,n-1):
            res=max(abs(subx1[i]-subn2[i+1]),abs(subn1[i]-subx2[i+1]),res)
        return res       


#Test Case:
sol=Solution()
lst=[-4,1,2,-3,1]
print(sol.maxDiffSubArray(lst))
