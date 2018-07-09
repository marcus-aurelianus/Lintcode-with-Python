class Solution:
    def twoSum(self,numbers,target):
        v_tab=dict((v,i) for i,v in enumerate(numbers))
        for i in range(len(numbers)):
            if target-numbers[i] in v_tab:
                return [i,v_tab[target-numbers[i]]]
        return [-1,-1]
            
#Test Case:
sol=Solution()
lst=[2,7,11,15]
print(sol.twoSum(lst,9))
