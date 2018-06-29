class Solution:
    def recoverRotatedSortedArray(self,nums):
        n=len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                nums[i+1:],nums[:i+1]=nums[:i+1],nums[i+1:]
                
#Test Case
sol=Solution()
lst=[4,5,6,7,8,9,1,2,3]
sol.recoverRotatedSortedArray(lst)
print(lst)
        
