class Solution:
    def subsets(self,nums):#iterative
        result=[[]]
        nums.sort()
        for num in nums:
            result.extend([ele+[num] for ele in result])
        return result
    def subsets1(self,nums):#recursive
        if nums:
            rest=self.subsets1(nums[1:])
            return rest+[[nums[0]]+x for x in rest]
        return [[]]
#Test Cases:  
sol=Solution()
print(sol.subsets([4,1,0]))
