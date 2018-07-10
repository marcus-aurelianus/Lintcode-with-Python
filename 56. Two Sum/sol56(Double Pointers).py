class Solution:
    def twoSum(self,numbers,target):
        numbers.sort()
        left,right=0,len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left,right]
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1
        return [-1,-1]
            
#Test Case:
sol=Solution()
lst=[2,7,11,15]
print(sol.twoSum(lst,9))
