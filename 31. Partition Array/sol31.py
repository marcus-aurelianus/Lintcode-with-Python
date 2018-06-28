class Solution:
    def partitionArray(self,nums,k):
        start,end=0,len(nums)-1
        while(start<=end):
            while start<=end and nums[start]<k:
                start+=1
            while start<=end and nums[end]>=k:
                end-=1
            if start<=end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        return start




#Test Case
sol=Solution()
lst=[1,1,1,1,3,1,1,1,2,2,1]
print(sol.partitionArray(lst,2))
print(lst)
        
