class Solution:
    def threeSum(self,numbers):
        numbers.sort()
        out=[]
        for i in range (len(numbers)):
            res=self.twoSum(numbers[i+1:],-numbers[i])
            if res:
                out.append(tuple([numbers[i]]+res))
        return out

    def twoSum(self,numbers,target):
        numbers.sort()
        left,right=0,len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                return [numbers[left],numbers[right]]
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1

#Test Case:
sol=Solution()
lst=[-1,0,1,2,-1,-4]
print(sol.threeSum(lst))
