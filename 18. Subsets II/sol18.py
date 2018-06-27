class Solution:
    def subsets(self,nums):#iterative
        result=[[]]
        for num in nums:
            result.extend([ele+[num] for ele in result if ele+[num] not in result])
        return result
    def subsets1(self,nums):#recursive
        if nums:
            rest=self.subsets1(nums[1:])
            return rest+[[nums[0]]+x for x in rest if [nums[0]]+x not in rest]
        return [[]]
#Test Cases:  
sol=Solution()
print(sol.subsets1([1,2,2,2]))
