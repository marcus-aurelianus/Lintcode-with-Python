class Solution:
    def fourSum(self,numbers,target):
        numbers.sort()
        out=[]
        for i in range(len(numbers)-3):
            for j in range(i+1,len(numbers)-2):
                res=self.twoSum(numbers[j+1:],target-numbers[i]-numbers[j])
                if res:
                    out.append([numbers[i],numbers[j]]+res)
        return out

    def twoSum(self,numbers,target):
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
lst=[1,0,-1,0,-2,2]
print(sol.fourSum(lst,0))
