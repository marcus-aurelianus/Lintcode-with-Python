class Solution:
    # @param num :  a list of integers
    # @return : a list of integers
    def nextPermuation(self, nums):
        n=len(nums)
        for i in range(n-2, -1, -1):
            if nums[i]<nums[i+1]:
                break
        else:
            nums.reverse()
            return nums
        for j in range(n-1,i,-1):
            if nums[i]<nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        for j in range(0, (n - i)//2):
            nums[i+j+1], nums[n-j-1] = nums[n-j-1], nums[i+j+1]
        return nums

#Test Case:
sol=Solution()
lst=[4, 0, 3, 9, 8, 7, 2, 1]
print(sol.nextPermuation(lst))
