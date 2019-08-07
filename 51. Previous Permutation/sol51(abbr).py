class Solution:
    # @param nums :  a list of integer
    # @return : a list of integer
    def previousPermuation(self, nums):
        # write your code here
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                break
        else:
            nums.reverse()
            return nums
        for j in range(len(nums)-1, i, -1):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        for j in range(0, (len(nums) - i)//2):
            nums[i+j+1], nums[len(nums)-j-1] = nums[len(nums)-j-1], nums[i+j+1]
        return nums


#Test Case:
sol=Solution()
lst=[1,3,2]
print(sol.previousPermuation(lst))
