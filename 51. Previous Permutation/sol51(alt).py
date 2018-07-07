
class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def previousPermuation(self, nums):
        # write your code here
        peakInd = len(nums) - 1
        
        while peakInd>0 and nums[peakInd] >= nums[peakInd - 1]:
            peakInd -=1
        peakInd -=1
        if peakInd >=0:
            swapInd = peakInd + 1
            while swapInd< len(nums) and nums[peakInd] > nums[swapInd]:
                swapInd +=1
            swapInd -=1
            nums[swapInd],nums[peakInd] =nums[peakInd] ,nums[swapInd]
        left = peakInd + 1
        right = len(nums) - 1
        while left< right:
            nums[left],nums[right] = nums[right],nums[left]
            left +=1
            right -=1
        return nums

#Test Case:
sol=Solution()
lst=[1,3,2]
print(sol.previousPermuation(lst))
