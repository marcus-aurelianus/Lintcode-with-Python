class Solution:
    def threeSumClosest(self,numbers,target):
        numbers.sort()
        out=None
        for i in range (len(numbers)-2):
            res=self.twoSum(numbers[i+1:],-numbers[i])
            temp=sum(res)+numbers[i]
            if out is None or abs(temp-target)<abs(out-target):
                out=temp
        return out

    def twoSum(self,numbers,target):
        left,right=0,len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target or left==right-1:
                return [numbers[left],numbers[right]]
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1

#Test Case:
sol=Solution()
lst=[-1,2,1,-4]
print(sol.threeSumClosest(lst,2))
